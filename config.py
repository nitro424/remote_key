"""
Configuration constants can be defined here or as env vars
env vars overrite values 

CRYPT_STORE_PATH: str
    full pyth of store file i.e. "/home/user/store"
BIND_ADDRESS: str
    http listen address i.e. "0.0.0.0" or "127.0.0.1"
BIND_PORT: int
    http listen port ie. 8000
DAEMON: bool
    Run as daemon (True|False)
    Docker should use False
"""
import os

CRYPT_STORE_PATH = "/home/user/store"
BIND_ADDRESS = "0.0.0.0"
BIND_PORT = 8000
DAEMON = True

# Env vars overrite config
if os.environ.get("CRYPT_STORE_PATH"):
    CRYPT_STORE_PATH = os.environ.get("CRYPT_STORE_PATH")
if os.environ.get("BIND_ADDRESS"):
    BIND_ADDRESS = os.environ.get("BIND_ADDRESS")
if os.environ.get("BIND_PORT"):
    BIND_PORT = int(os.environ.get("BIND_PORT"))
if os.environ.get("DAEMON"):
    DAEMON = os.environ.get("DAEMON") == "True"
