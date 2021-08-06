from awsmfaprofile.config import ENV_VARS
from sys import platform
import click

def show_commands(token_dict):
    click.echo("\nCopy and execute the following on your command line or re-run with --persist flag to update or add an aws profile\n")
    click.echo("-"*50)
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        # linux or osx
        for key, val in ENV_VARS.items():
            click.echo(f"export {key}={token_dict.get(val)}")
    elif platform == "win32":
        # Windows...
        for key, val in ENV_VARS.items():
            click.echo(f"SET {key}={token_dict.get(val)}")
    click.echo("-"*50)