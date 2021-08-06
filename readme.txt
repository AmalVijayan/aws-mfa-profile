
Prerequisites
-------------
  - AWSCLI v2
  - AWS user profile
  - Python >=3.6
  - pip >= 21.1.3

Installation
------------

    Create a virtual environment:
    -----------------------------
      - python -m venv <env_name>
      or
      - virtualenv <env_name> [Requires virtualenv to be installed]

    Activate virtual environment
    ----------------------------
    Linux or OSX:
      - source <env_name>/bin/activate
    Windows
      - <env_name>/Scripts/activate
    
    Test installation build: [Optional] 
      - pip install --use-feature=in-tree-build .

    Install
    -------
    Note : To be executed inside project root where setup.py resides
    - pip install .

Uninstall
---------

    Activate virtual environment
    ----------------------------
    Linux or OSX:
      - source <env_name>/bin/activate
    Windows
      - <env_name>/Scripts/activate

    Uninstall
    ---------
      - pip uninstall awsmfaprofile

Usage
-----

Usage: my-cli [OPTIONS] COMMAND [ARGS]...

Options:

  --help  Show this message and exit.


    Usage: my-cli awsmfa [OPTIONS]

    eg. my-cli awsmfa --profile=<> --serial-number=arn:aws:iam::<id>:mfa/<user> --token=<> -P -profile-name=<new_profile_name>

Options:
  -p, --profile TEXT        The name of the profile to be used for creating   
                            the mfa profile. Defaulted to the value set to    
                            AWS_PROFILE environment variable.
  -s, --serial-number TEXT  The value is either the serial number for a       
                            hardware device (such as GAHT12345678 ) or an     
                            Amazon Resource Name (ARN) for a virtual device   
                            (such as arn:aws:iam::123456789012:mfa/user       
                            [required]
  -t, --token TEXT          The multidigit pin provided by the MFA device.    
                            [required]
  -c, --config-path TEXT    The directory path of the aws profile eg.
                            /home/user/.aws or C:\Users\user\.aws  
  -P, --persist             If set, an aws profile is created and appended to 
                            the aws credentials file. --profile-name option is
                            required with --persist option. Profile existing  
                            with the same name will be updated.
  -n, --profile-name TEXT   The name for the new aws profile to be created.   
                            Profile existing with the same name will be
                            updated. NOTE: This argument is mutually inclusive
                            with persist
  --help                    Show this message and exit.