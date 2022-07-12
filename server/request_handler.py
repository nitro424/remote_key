"""
TODO: doc-string
"""
from http.server import BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):
    """
    TODO: doc-string
    """

    key = ""

    def do_GET(self):
        """
        TODO: doc-string"""
        print("GET")
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(RequestHandler.key.encode("utf-8"))
            return

        self.send_error(404)
