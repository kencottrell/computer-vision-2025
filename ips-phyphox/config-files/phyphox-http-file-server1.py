import http.server
import socketserver
import os
PORT = 8000


# Set the directory to serve files from
os.chdir('/path/to/your/directory')

Handler = http.server.SimpleHTTPRequestHandler



with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()


    '''
    python3 -m http.server --bind 0.0.0.0 8000

    '''
