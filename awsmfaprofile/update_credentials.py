import configparser
import os

config = configparser.ConfigParser()

def write_credentials(config_path, token_dict, parent_profile):
    new_profile_name = f"{parent_profile}-mfa"
    cre_file = f'{config_path}{os.sep}credentials'
    config.read(cre_file)
    config[new_profile_name] = {'aws_access_key_id': token_dict['access_key'],
                                'aws_secret_access_key': token_dict['secret_key'],
                                'aws_session_token': token_dict['session_token']}
    with open(cre_file, 'w') as configfile:
        config.write(configfile)