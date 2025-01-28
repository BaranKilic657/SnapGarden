# server.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from sign_up_handler import handle_signup
from sign_in_handler import handle_signin

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        """Override log_message to include detailed logs"""
        print(f"{self.client_address[0]} - [{self.log_date_time_string()}] {format % args}")

    def do_OPTIONS(self):
        """Handle preflight CORS requests"""
        self.log_message("OPTIONS request received")
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        """Handle POST requests for /signup and /signin"""
        self.log_message(f"POST request received for path: {self.path}")
        if self.path == "/signup":
            self._handle_request(handle_signup)
        elif self.path == "/signin":
            self._handle_request(handle_signin)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')  # Added
            self.end_headers()
            response = {'status': 'error', 'message': 'Not Found'}
            self.wfile.write(json.dumps(response).encode())

    def _handle_request(self, handler_function):
        """Common logic for handling POST requests"""
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            self.log_message(f"Request Data: {post_data.decode('utf-8')}")

            data = json.loads(post_data)
            self.log_message(f"Parsed JSON Data: {data}")

            response = handler_function(data)
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')  # Moved here
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        except json.JSONDecodeError as e:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')  # Added
            self.end_headers()
            error_response = {'status': 'error', 'message': 'Invalid JSON format'}
            self.log_message(f"Response: {error_response}")
            self.wfile.write(json.dumps(error_response).encode())

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')  # Added
            self.end_headers()
            error_response = {'status': 'error', 'message': str(e)}
            self.log_message(f"Response: {error_response}")
            self.wfile.write(json.dumps(error_response).encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    """Start the HTTP server"""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on http://localhost:{port}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.server_close()

if __name__ == "__main__":
    run()
