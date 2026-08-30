from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from src.greeting import greeting


def handle_request(path: str) -> tuple[int,
  str]:
      parsed = urlparse(path)

      if parsed.path != "/greet":
          return 404, "Not Found"
          
      query = parse_qs(parsed.query)
      name = query.get("name", [""])[0]

      return 200, greeting(name)


class GreetingHandler(BaseHTTPRequestHandler):
      def do_GET(self):
          status, body = handle_request(self.path)
          self.send_response(status)
          self.send_header("Content-Type","text/plain")
          self.end_headers()
          self.wfile.write(body.encode())


if __name__ == "__main__":
      server = HTTPServer(("localhost", 8000),GreetingHandler)
      server.serve_forever()