import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

DEFAULT_PORT = 8080


class PingHandler(BaseHTTPRequestHandler):
    def _send_empty(self, status):
        self.send_response(status)
        self.end_headers()

    def do_GET(self):
        if self.path != "/ping":
            print("buh")
            self._send_empty(404)
            return

        body = json.dumps(dict(self.headers.items())).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _not_found(self):
        self._send_empty(404)

    # Toute autre méthode HTTP renvoie 404 (corps vide)
    do_POST = do_PUT = do_DELETE = do_PATCH = do_HEAD = do_OPTIONS = _not_found


def main():
    port = int(os.environ.get("PING_LISTEN_PORT", DEFAULT_PORT))
    server = HTTPServer(("localhost", port), PingHandler)
    print(f"Serveur en écoute sur http://localhost:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()


if __name__ == "__main__":
    main()