from awsmfaprofile.update_credentials import write_credentials
from awsmfaprofile.get_session_token import get_token
import click
import os

@click.command()
@click.option('--parent_profile', default=os.getenv("AWS_PROFILE") , help='The name of the profile to be used for creating the mfa profile. Defaulted to the value set to AWS_PROFILE environment variable. eg. profile-mfa')
@click.option('--serial_number' , help='The value is either the serial number for a hardware device (such as GAHT12345678 ) or an Amazon Resource Name (ARN) for a virtual device (such as arn:aws:iam::123456789012:mfa/user', required=True)
@click.option('--auth_token' , help='The multidig pin provided by the MFA device, if the trust policy of the role being assumed requires MFA.', required=True)
@click.option('--display', default=True , help='The directory path of the aws profile eg. /home/user/.aws or C:\\Users\\user\\.aws')
@click.option('--write_to_credentials', default=False , help='If set to True will append the generated profile to the aws credentials file')
@click.option('--config_path', default=f'{os.path.expanduser("~")}{os.sep}.aws' , help='The directory path of the aws profile eg. /home/user/.aws or C:\\Users\\user\\.aws')
def create(parent_profile, serial_number, auth_token, display, write_to_credentials, config_path):
    

    click.echo('updating environment variables ..') 

    if parent_profile:
        os.environ["AWS_PROFILE"]=parent_profile

    status, token_dict = get_token(serial_number, auth_token)

    if status :
        click.echo("successfully retrieved token!")
        if write_to_credentials:
            write_credentials(config_path, token_dict, parent_profile)
        
        if display:

            click.echo("copy and paste the following to ~/.aws/credentials or re run the code with --write_to_credentials=True")
            click.echo("")
            click.echo("-"*50)
            click.echo(f"[{parent_profile}-mfa]")
            click.echo(f"aws_access_key_id = {token_dict.get('access_key')}")
            click.echo(f"aws_secret_access_key = {token_dict.get('secret_key')}")
            click.echo(f"aws_session_token = {token_dict.get('session_token')}")
            click.echo("-"*50)

       
# aws-mfa-profile --serial_number="" --parent_profile="vonnue" --auth_token="" --write_to_credentials=True
