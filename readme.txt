
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

    Usage: aws-mfa-profile [OPTIONS]

    eg. aws-mfa-profile --serial_number="arn:aws:iam::<id>:mfa/<user>" --parent_profile="<>" --auth_token="<>" --write_to_credentials=True


Options:

  --parent_profile TEXT           The name of the profile to be used for
                                  creating the mfa profile. Defaulted to the
                                  value set to AWS_PROFILE environment
                                  variable. eg. profile-mfa
  --serial_number TEXT            The value is either the serial number for a
                                  hardware device (such as GAHT12345678 ) or
                                  an Amazon Resource Name (ARN) for a virtual
                                  device (such as
                                  arn:aws:iam::123456789012:mfa/user
                                  [required]
  --auth_token TEXT               The multidig pin provided by the MFA device,
                                  if the trust policy of the role being
                                  assumed requires MFA.  [required]
  --display BOOLEAN               The directory path of the aws profile eg.
                                  /home/user/.aws or C:\Users\user\.aws
  --write_to_credentials BOOLEAN  If set to True will append the generated
                                  profile to the aws credentials file
  --config_path TEXT              The directory path of the aws profile eg.
                                  /home/user/.aws or C:\Users\user\.aws
  --help                          Show this message and exit.