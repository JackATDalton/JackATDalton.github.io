#!/usr/bin/env python3
"""
Local dev server with Jekyll-style template injection.
Reads _layouts/ and _includes/ to assemble pages on the fly,
matching what GitHub Pages / Jekyll produces.

Run: python3 local-server.py
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import re
import io

PORT = 8000
DIRECTORY = "."


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def parse_front_matter(content):
    """Strip YAML front matter and return (metadata dict, body string)."""
    if not content.startswith("---"):
        return {}, content
    end = content.index("---", 3)
    front = content[3:end].strip()
    body = content[end + 3:].strip()
    meta = {}
    for line in front.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip()
    return meta, body


def resolve_includes(html):
    """Replace {% include filename.html %} with file contents from _includes/."""
    def replacer(m):
        name = m.group(1).strip()
        path = os.path.join("_includes", name)
        return read(path) if os.path.exists(path) else ""
    return re.sub(r"\{%\s*include\s+(\S+)\s*%\}", replacer, html)


def render(page_path):
    """Assemble a page by injecting it into its layout."""
    content = read(page_path)
    meta, body = parse_front_matter(content)

    layout_name = meta.get("layout", "default")
    layout_path = os.path.join("_layouts", f"{layout_name}.html")

    if not os.path.exists(layout_path):
        return body.encode("utf-8")

    layout = read(layout_path)
    title = meta.get("title", "Jack Dalton")

    html = layout
    html = resolve_includes(html)
    html = html.replace("{{ content }}", body)
    html = html.replace("{{ page.title }}", title)

    return html.encode("utf-8")


class JekyllHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def do_GET(self):
        # Normalise path
        path = self.path.split("?")[0].split("#")[0]
        if path == "/" or path == "/index.html":
            path = "/index.html"
        elif not os.path.splitext(path)[1]:
            path = path.rstrip("/") + ".html"

        file_path = path.lstrip("/")

        # Serve HTML files through the Jekyll renderer
        if path.endswith(".html") and os.path.exists(file_path):
            try:
                data = render(file_path)
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
            except Exception as e:
                self.send_error(500, str(e))
            return

        # Everything else (CSS, images, fonts) served normally
        return super().do_GET()

    def log_message(self, fmt, *args):
        print(f"  {self.address_string()} {fmt % args}")


def start_server():
    try:
        with socketserver.TCPServer(("", PORT), JekyllHandler) as httpd:
            httpd.allow_reuse_address = True
            print(f"Dev server running at http://localhost:{PORT}")
            print("Ctrl+C to stop")
            try:
                webbrowser.open(f"http://localhost:{PORT}")
            except Exception:
                pass
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:
            print(f"Port {PORT} already in use. Run: lsof -ti:{PORT} | xargs kill")
        else:
            print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    start_server()
