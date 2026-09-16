from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

value = ""


class Handler(SimpleHTTPRequestHandler):

    def do_GET(self):
        global value

        parsed = urlparse(self.path)

        if parsed.path == "/set":
            params = parse_qs(parsed.query)
            value = params.get("value", [""])[0]

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
            return

        if parsed.path == "/value":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(value.encode())
            return

        if parsed.path == "/reset":
            value = ""

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
            return


        return super().do_GET()


server = HTTPServer(("0.0.0.0", 8080), Handler)

print("Server running on port 8080")
server.serve_forever()