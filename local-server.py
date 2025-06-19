#!/usr/bin/env python3
"""
Simple HTTP server for local development testing.
Run this script to serve your Jekyll website locally.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

# Configuration
PORT = 8000
DIRECTORY = "."

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Add cache control headers for development
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        # Handle Jekyll-style URLs
        if self.path == '/' or self.path == '/index.html':
            self.path = '/index.html'
        elif not '.' in self.path.split('/')[-1]:
            # If no file extension, try to serve as HTML
            self.path = self.path.rstrip('/') + '.html'
        
        return super().do_GET()

def start_server():
    """Start the local development server."""
    try:
        with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
            print("🚀 Jack Dalton's Portfolio Development Server")
            print("=" * 50)
            print(f"📍 Server URL: http://localhost:{PORT}")
            print(f"📁 Serving from: {os.path.abspath(DIRECTORY)}")
            print("💡 Press Ctrl+C to stop the server")
            print("-" * 50)
            
            # Try to open browser automatically
            try:
                webbrowser.open(f'http://localhost:{PORT}')
                print("🌐 Opening browser automatically...")
            except:
                print(f"🌐 Please open http://localhost:{PORT} in your browser")
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {PORT} is already in use.")
            print(f"💡 Try running: lsof -ti:{PORT} | xargs kill")
            sys.exit(1)
        else:
            print(f"❌ Error starting server: {e}")
            sys.exit(1)

if __name__ == "__main__":
    print("Starting Jack Dalton's Portfolio Server...")
    start_server()
