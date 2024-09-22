# main.py
from audio_input import start_audio_stream
from audio_websocket import start_server

import threading
import http.server
import socketserver

# Function to start the HTTP server
def start_http_server():
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving HTTP on port {PORT}")
        httpd.serve_forever()

# Start the audio input and processing stream
audio_thread = threading.Thread(target=start_audio_stream)
audio_thread.start()

# Start the WebSocket server
websocket_thread = threading.Thread(target=start_server)
websocket_thread.start()

# Start the HTTP server
http_thread = threading.Thread(target=start_http_server)
http_thread.start()

# Keep the main thread alive
audio_thread.join()
websocket_thread.join()
http_thread.join()
