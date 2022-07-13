"""
This module provides a custom http request handler derived from BaseHTTPRequestHandler
"""
from http.server import BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):
    """
    This request handler only serves a key on GET /
    """

    key = ""

    def do_GET(self):
        """
        Provides a key in plain text utf-8 on GET /
        """
        print("GET")
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(RequestHandler.key.encode("utf-8"))
            return

        self.send_error(404)
