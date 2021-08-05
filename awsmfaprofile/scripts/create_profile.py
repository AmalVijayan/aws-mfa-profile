from awsmfaprofile.set_aws_env import set_env
from awsmfaprofile.config import ENV_VARS
from awsmfaprofile.get_session_token import get_token
import click
import os

@click.command()
@click.option('--parent_profile', default=os.getenv("AWS_PROFILE") , help='The name of the profile to be used for creating the mfa profile. Defaulted to the value set to AWS_PROFILE environment variable. eg. profile-mfa')
@click.option('--serial_number' , help='The value is either the serial number for a hardware device (such as GAHT12345678 ) or an Amazon Resource Name (ARN) for a virtual device (such as arn:aws:iam::123456789012:mfa/user', required=True)
@click.option('--auth_token' , help='The multidig pin provided by the MFA device, if the trust policy of the role being assumed requires MFA.', required=True)
@click.option('--display', default=False , help='The directory path of the aws profile eg. /home/user/.aws or C:\\Users\\user\\.aws')
def create(parent_profile, serial_number, auth_token, display):
    

    click.echo('updating environment variables ..') 

    if parent_profile:
        os.environ["AWS_PROFILE"]=parent_profile

    _, token_dict = get_token(serial_number, auth_token)
    status, resp = set_env(token_dict)

    if status :
        click.echo(resp)
        if display:
            click.echo(f"[{parent_profile}-mfa]")
            for key,val in ENV_VARS.items():
                click.echo(f"{val} = {os.environ.get(key)}")
       