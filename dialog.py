"""
Provides functions to interact with user in terms of asking fpr secrets and creating the store.
"""
import os
import sys
from sys import stderr
from getpass import getpass
from store import create_store, read_key


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


def store_found_dialog(path: str):
    """
    Executed when store file is found
    Asks for store password and extracts key

    Parameters
    path: str
        location of store file

    Returns
    str
        the decrypted key from store file
    """
    print(f"Found store in {path}")
    key = False
    while not key:
        password = get_secret_dialog(do_check=False)
        key = read_key(path, password)

        if not key:
            os.system("clear")
            print("Wrong password. Try again.")
    return key


def store_not_found_dialog(path: str):
    """
    Executed when store file not found
    Asks for password and key to create a new store file

    Parameters
    path: str
        location of store file

    Returns
    str
        the decrypted key from store file

    """
    do_create = input(f"No store present in {path}. Create? (y/n): ")
    if do_create.lower() != "y":
        sys.exit(0)

    password = get_secret_dialog()
    key = get_secret_dialog("secret key")
    create_store_dialog(path, key, password)

    return key
