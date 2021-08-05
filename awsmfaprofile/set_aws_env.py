import os
from .config import ENV_VARS
import click 
from sys import platform
import subprocess

def set_env(token_response_dict):
    try:
        for key in ENV_VARS.keys():
            os.environ[key]=token_response_dict[ENV_VARS[key]]
            click.echo(f"{key} ✓")
        return 1, "successfully set environment!"
    except Exception as e:
        click.echo(e)
        exit()
        



