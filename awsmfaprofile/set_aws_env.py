import os
from .config import ENV_VARS
import click 
from sys import platform
import subprocess

def set_env(token_response_dict):
    try:
        for key in ENV_VARS.keys():
            # os.environ[key]=token_response_dict[ENV_VARS[key]]
            if platform == "linux" or platform == "linux2" or platform == "darwin":
                # linux
                process = subprocess.Popen(["export",f"{key}","2","=", f"{token_response_dict[ENV_VARS[key]]}"], stdout=subprocess.PIPE)
                # os.system(f"export {key}={token_response_dict[ENV_VARS[key]]}")
            elif platform == "win32":
                # Windows...
                process = subprocess.Popen(["SET",f"{key}","2","=", f"{token_response_dict[ENV_VARS[key]]}"], stdout=subprocess.PIPE)
                # os.system(f"SET {key}={token_response_dict[ENV_VARS[key]]}")
            process.communicate()[0]
            click.echo(f"{key} ✓")
        return 1, "successfully set environment!"
    except Exception as e:
        click.echo(e)
        # return 0, f"{e}"
        exit()
        



