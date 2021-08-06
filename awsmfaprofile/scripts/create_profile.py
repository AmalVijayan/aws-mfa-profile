from awsmfaprofile.display_commands import show_commands
from awsmfaprofile.update_credentials import write_credentials
from awsmfaprofile.get_session_token import get_token
import click
import os

class RequiredIf(click.Option):

    def __init__(self, *args, **kwargs):
        self.required_if = kwargs.pop('required_if')
        assert self.required_if, "'required_if' parameter required"
        kwargs['help'] = (kwargs.get('help', '') +
                          ' NOTE: This argument is mutually inclusive with %s' %
                          self.required_if
                          ).strip()
        super(RequiredIf, self).__init__(*args, **kwargs)

    def handle_parse_result(self, ctx, opts, args):
        click.echo('')
        if self.required_if in opts:
            if self.name not in opts:
                raise click.UsageError(
                    " Illegal usage. `%s` must be passed with `%s` flag" % (self.name, self.required_if))
            else:
                self.prompt = None

        return super(RequiredIf, self).handle_parse_result(
            ctx, opts, args)


@click.group()
def cli():
    pass

@click.option('-p', '--profile', default=os.getenv("AWS_PROFILE"), show_default=True, 
              help='The name of the profile to be used for creating the mfa profile. Defaulted to the value set to AWS_PROFILE environment variable.')
@click.option('-s', '--serial-number', required=True,
              help='The value is either the serial number for a hardware device (such as GAHT12345678 ) or an Amazon Resource Name (ARN) for a virtual device (such as arn:aws:iam::123456789012:mfa/user')
@click.option('-t', '--token', required=True,
              help='The multidigit pin provided by the MFA device.')
@click.option('-c', '--config-path', default=f'{os.path.expanduser("~")}{os.sep}.aws', show_default=True,
             help='The directory path of the aws profile eg. /home/user/.aws or C:\\Users\\user\\.aws')
@click.option('-P', '--persist', is_flag=True,
                help='If set, an aws profile is created and appended to the aws credentials file. --profile-name option is required with --persist option. Profile existing with the same name will be updated.')
@click.option('-n', '--profile-name', cls=RequiredIf, required_if='persist',
              help='The name for the new aws profile to be created. Profile existing with the same name will be updated.')
@cli.command()
def awsmfa(profile, serial_number, token, profile_name, config_path, persist=False):

    if not profile:
        click.echo('\nError. Unable to authenticate with AWS. set a profile using --profile or set AWS_PROFILE environment!')
        exit()

    click.echo(f'AWS profile in use : {profile}')
    os.environ["AWS_PROFILE"] = profile

    click.echo('\nRetieving token ..')
    status, token_dict = get_token(serial_number, token)

    if status:
        click.echo("successfully retrieved token!")

        if persist:
            write_credentials(config_path, token_dict, profile_name)
        else:
            show_commands(token_dict)
    exit()
