from boto.sts import STSConnection
import click

def get_token(mfa_serial_number, mfa_token):
    sts_connection = STSConnection()
    try:
        response = sts_connection.get_session_token(
            duration=43200,
            mfa_serial_number=mfa_serial_number, 
            mfa_token=mfa_token,
        )
        return 1, response.__dict__
    except Exception as e:
        click.echo(e)
        exit()
