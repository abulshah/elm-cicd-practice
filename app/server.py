
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

APP_VERSION = os.getenv("APP_VERSION", "1.0")

def get_version():
    return APP_VERSION

def get_status():
    return 200

class PulseHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            status, body = get_status(), "healthy"

        elif self.path == "/version":
            status, body = 200, get_version()

        else:
            status, body = 404, "not found"

        payload = body.encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

if __name__ == "__main__":
    ThreadingHTTPServer(
        ("127.0.0.1", 8000), PulseHandler
    ).serve_forever()
