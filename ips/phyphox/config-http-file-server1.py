import http.server
import socketserver
import os
import importlib

module = importlib.import_module('settings')  # ken's iphone ip


PORT = module.PORT
CONFIG_DIR = module.CONFIG_DIR
CONFIG_FILE = module.CONFIG_FILE
# type into browser: http://localhost:8000/


# Set the directory to serve files from
os.chdir(CONFIG_DIR)

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()


    '''
    python3 -m http.server --bind 0.0.0.0 8000

    '''
