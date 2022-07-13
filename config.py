"""
Configuration constants

CRYPT_STORE_PATH: str
    full pyth of store file i.e. "/home/user/store"
BIND_ADDRESS: str
    http listen address i.e. "0.0.0.0" or "127.0.0.1"
BIND_PORT: int
    http listen port ie. 8000
"""
CRYPT_STORE_PATH = "/home/user/store"
BIND_ADDRESS = "0.0.0.0"
BIND_PORT = 8000


# Env vars overrite config
import os

CRYPT_STORE_PATH = os.environ.get("CRYPT_STORE_PATH") or CRYPT_STORE_PATH
BIND_ADDRESS = os.environ.get("BIND_ADDRESS") or BIND_ADDRESS
BIND_PORT = os.environ.get("BIND_PORT") or BIND_PORT
