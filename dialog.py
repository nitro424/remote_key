"""
Provides functions to interact with user in terms of asking fpr secrets and creating the store.
"""
import os
import sys
from sys import stderr
from getpass import getpass
from crypt_store import create_store


def get_secret_dialog(secret_type="password", do_check=True):
    """
    Asks for secrets (password or key)

    Parameters
    secret_type: str
        Specifies the type of secret (password | secret key)
    do_check: bool
        Ask twice for a secret to check the input

    Returns
    str
        the secret
    """
    while True:
        secret = getpass(f"Please provide {secret_type}: ")
        if do_check:
            secret_check = getpass(f"Please provide {secret_type} again: ")
        if do_check and secret != secret_check:
            os.system("clear")
            print("Not matching. Try again.")
        else:
            return secret


def create_store_dialog(path: str, key: str, password: str):
    """
    Creates the store

    Parameters
    path: str
        Path of the store
    key: str
        Key that will be saved encrypted in the store
    password: str
        Password which will be uses to encrypt the store
    """
    print(f"Creating store {path} ... ", end="")
    try:
        create_store(path, key, password)
    except Exception as exp:
        print(exp, file=stderr)
        sys.exit(1)
    print("ok")
