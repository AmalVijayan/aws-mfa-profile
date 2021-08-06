from setuptools import setup, find_packages

setup(
    name='awsmfaprofile',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'boto'
    ],
    entry_points={
        'console_scripts': [
            'my-cli = awsmfaprofile.scripts.create_profile:cli',
        ],
    },
)