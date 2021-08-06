import configparser
import os

import click

config = configparser.ConfigParser()

def write_credentials(config_path, token_dict, profile_name):
    click.echo(f"\nWARNING: Using an existing profile name can result in overwriting of aws credentials. Make sure to provide the right profile name")
    new_profile_name = f"{profile_name}"
    cre_file = f'{config_path}{os.sep}credentials'
    config.read(cre_file)
    config[new_profile_name] = {'aws_access_key_id': token_dict['access_key'],
                                'aws_secret_access_key': token_dict['secret_key'],
                                'aws_session_token': token_dict['session_token']}
    with open(cre_file, 'w') as configfile:
        config.write(configfile)

    click.echo(f"\nAWS profile created : {profile_name}")
    click.echo(f"\nExecute the following command to use the the ")
