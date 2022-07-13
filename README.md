# remote_key

remote_key is a tool that serves a key via http to other applications. The key is locally stored password protected. The tool asks for a password on every start to open the crypted store file and extract the key to serve.

## Installation

### Prerequisites

#### Ubuntu

```bash
sudo apt install python3-pip python3-venv git
```

#### Fedora

```bash
sudo dnf in python3-pip git
```

### Clone repo

```bash
git clone https://github.com/nitro424/remote_key.git
```

### Create and activate python virtual environment

```bash
python3 -m venv remote_key/venv
source remote_key/venv/bin/activate
```

### Install python dependencies

Make sure the python virtual environment is activated.

```bash
pip install -r remote_key/requirements.txt
```

## Configuration

Configuration is kept in `remote_key/config.py`.

config.py

```python
CRYPT_STORE_PATH = "/home/user/store"
BIND_ADDRESS = "0.0.0.0"
BIND_PORT = 8000
DAEMON = True
```

-   CRYPT_STORE_PATH

    Specify the path of the store file. Write permissions needed.

-   BIND_ADDRESS

    The http server will listen to that address. Useful values are `"0.0.0.0"` when direct access is needed or `"120.0.0.1"` when using a reverse proxy.

-   BIND_PORT

    Thehttp server will listen to that port. Value is type of int.

-   DAEMON

    Sets the http server to daemon mode to be able to exit the shell after start. Makes no sense when running in docker. Value is type of bool (`True`|`False`).

Every value can also set using environment variables. This is useful in docker mode.

## Run the program

Make sure the python virtual environment is activated.

```bash
source remote_key/venv/bin/activate
```

The just run the program as follows.

```bash
python remote_key
```
