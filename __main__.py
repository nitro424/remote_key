#!/usr/bin/env python3
"""
Package created crypted key store and a http server to serve the crypted key
"""
import os
import sys
import daemon
import config
import dialog
from server import server


def main():
    """
    start of package
    create key store, open key store and get key to start http server
    """
    try:
        if os.path.isdir(config.CRYPT_STORE_PATH):
            print(f"{config.CRYPT_STORE_PATH} is not a file", file=sys.stderr)
            sys.exit(1)
        if not os.path.exists(config.CRYPT_STORE_PATH):
            key = dialog.store_not_found_dialog(config.CRYPT_STORE_PATH)
        else:
            key = dialog.store_found_dialog(config.CRYPT_STORE_PATH)
    except KeyboardInterrupt:
        print("Exiting")
        sys.exit(0)

    start_server(key)


def start_server(key: str):
    """
    Start and daemonize http server

    Parameters
    key: str
        the key to serve
    """
    print(f"Serving key at http://{config.BIND_ADDRESS}:{config.BIND_PORT}/")
    print("Please use a reverse proxy to secure communiaction with https")
    print("Daemonizing...")
    with daemon.DaemonContext():
        server.run(key, bind_address=config.BIND_ADDRESS, bind_port=config.BIND_PORT)


main()
