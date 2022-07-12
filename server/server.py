"""
Simple http server to provide the key
"""
import sys
from http.server import HTTPServer
from .request_handler import RequestHandler


def run(key: str, bind_address: str, bind_port: int):
    """
    Starts the http server

    Parameters
    key: str
        The key to provide on /
    bind_address: str
        The address to listen on
    bind_port: int
        The port the listen on
    """
    RequestHandler.key = key
    server_address = (bind_address, bind_port)
    httpd = HTTPServer(server_address, RequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nExiting")
        exit(0)
    except Exception:
        print("\nExiting")
        sys.exit(0)
