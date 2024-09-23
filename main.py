import threading
import http.server
import socketserver
import asyncio
from audio_input import start_audio_stream
from audio_websocket import start_websocket_server

# Function to start the HTTP server
def start_http_server():
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving HTTP on port {PORT}")
        httpd.serve_forever()

# Function to start the WebSocket server
async def start_websocket():
    await start_websocket_server()

# Start the audio input and processing stream
audio_thread = threading.Thread(target=start_audio_stream)
audio_thread.start()

# Start the HTTP server in a separate thread
http_thread = threading.Thread(target=start_http_server)
http_thread.start()

# Set up the asyncio event loop manually
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)  # Set the new loop as the current one

# Pass the event loop to the audio input module
import audio_input
audio_input.loop = loop  # Assign the loop to the global variable

# Run the WebSocket server on the main thread
loop.run_until_complete(start_websocket())
loop.run_forever()  # Keep the WebSocket server running
