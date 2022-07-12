#!/usr/bin/env python3
"""
TODO: module doc-string
"""
import os
import sys
import daemon
import config
import server
import dialog
from crypt_store import read_key


def store_found():
    """
    TODO: doc-string
    """
    print(f"Found store in {config.CRYPT_STORE_PATH}")
    key = False
    while not key:
        password = dialog.get_secret_dialog(do_check=False)
        key = read_key(config.CRYPT_STORE_PATH, password)
        if not key:
            os.system("clear")
            print("Wrong password. Try again.")
    return key


def store_not_found():
    """
    TODO: doc-string
    """
    do_create = input(f"No store present in {config.CRYPT_STORE_PATH}. Create? (y/n): ")
    if do_create.lower() != "y":
        sys.exit(0)

    password = dialog.get_secret_dialog()
    key = dialog.get_secret_dialog("secret key")
    dialog.create_store_dialog(config.CRYPT_STORE_PATH, key, password)

    return key


if not os.path.exists(config.CRYPT_STORE_PATH):
    secret_key = store_not_found()
else:
    secret_key = store_found()


print(f"Serving key http://{config.BIND_ADDRESS}:{config.BIND_PORT}/")
print("Daemonizing...")
with daemon.DaemonContext():
    server.run(secret_key, bind_address=config.BIND_ADDRESS, bind_port=config.BIND_PORT)
