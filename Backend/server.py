from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from sign_up_handler import handle_signup

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        # CORS Header für OPTIONS-Anfragen setzen
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')  # Alle Domains erlauben
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')  # Erlaubte Methoden
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')  # Erlaubte Header
        self.end_headers()

    def do_POST(self):
        if self.path == "/signup":
            # Lese die eingehende JSON-Daten
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            # Versuche, die JSON-Daten zu laden
            try:
                data = json.loads(post_data)
                response = handle_signup(data)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())
            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'error', 'message': 'Invalid JSON'}).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'error', 'message': 'Not found'}).encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on http://localhost:{port}')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
