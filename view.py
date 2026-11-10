#!/usr/bin/env python3
"""Open the ShapeTx flow-cytometry task visualizer: serves ./site on localhost and opens it in your browser.

    python3 view.py            # then press Ctrl+C to stop
"""
import functools
import http.server
import socket
import sys
import threading
import webbrowser
from pathlib import Path

SITE = Path(__file__).resolve().parent / "site"
port = next(p for p in range(8765, 8865) if socket.socket().connect_ex(("127.0.0.1", p)) != 0)
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(SITE))
handler.log_message = lambda *a, **k: None
server = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
url = f"http://localhost:{port}/index.html"
print(f"Visualizer running at {url}  (Ctrl+C to stop)", flush=True)
if "--no-browser" not in sys.argv:
    threading.Timer(0.5, lambda: webbrowser.open(url)).start()
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nstopped")
