from http.server import HTTPServer, SimpleHTTPRequestHandler

# Define the server's address and port
server_address = ('', 8000)

# Create a basic HTTP request handler
class MyRequestHandler(SimpleHTTPRequestHandler):
    pass

# Create the HTTP server
httpd = HTTPServer(server_address, MyRequestHandler)

# Start the server
print(f"Server running at http://{server_address[0]}:{server_address[1]}")
httpd.serve_forever()
