#!/usr/bin/env python3
"""
Voer dit uit in dezelfde map als index.html
Dan opent automatisch je browser op http://localhost:8000
"""

import http.server
import socketserver
import webbrowser
import os
import time

PORT = 8000
HANDLER = http.server.SimpleHTTPRequestHandler

# Start webserver
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), HANDLER) as httpd:
    url = f"http://localhost:{PORT}"
    print(f"Server draait op {url}")
    print("Toets CTRL+C om te stoppen")

    # Open browser
    time.sleep(0.5)
    try:
        webbrowser.open(url)
    except:
        print(f"Kun je niet automatisch openen? Ga handmatig naar {url}")

    httpd.serve_forever()
