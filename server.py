from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "127.0.0.1"
PORT = 8000

class CustomHandler(SimpleHTTPRequestHandler):
    pass

server = HTTPServer((HOST, PORT), CustomHandler)

print(f"Server running at http://{HOST}:{PORT}")
server.serve_forever()