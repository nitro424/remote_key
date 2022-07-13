"""
Provides functions to create a crypted store and read it.
"""
import cryptocode


def create_store(path: str, key: str, password: str):
    """
    creates a password protected store with a crypted key

    Parameters:
    path: str
        The path to the store
    key: str
        The key that will be encrypted inside the store
    password:
        The password to decrypt the store
    """
    with open(path, "w", encoding="utf-8") as store:
        store.write(cryptocode.encrypt(key, password))


def read_key(path: str, password: str):
    """
    Reads a crypted key from the store

    Parameters:
    path: str
        The path to the store
    password:
        The password to decrypt the store

    Returns
    str
        The decrypted key
    """
    with open(path, "r", encoding="utf-8") as store:
        return cryptocode.decrypt(store.read(), password)
