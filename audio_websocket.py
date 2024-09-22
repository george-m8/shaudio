# audio_websocket.py
# This bitch aint workin'

import asyncio
import websockets
import json

debug = True

# This bitch aint workin'

# Function to send audio data over WebSocket
async def send_audio_data(websocket, low_band, mid_band, high_band):
    # Convert NumPy float32 to Python float
    data = {
        "low": float(low_band),  # Convert to float
        "mid": float(mid_band),  # Convert to float
        "high": float(high_band)  # Convert to float
    }
    await websocket.send(json.dumps(data))  # Send data as a JSON object

# Function to run the WebSocket server
async def audio_server(websocket, path):
    if (debug): print("Client connected")
    try:
        while True:
            await asyncio.sleep(1)  # Keep connection alive
    except websockets.ConnectionClosed:
        print("Client disconnected")

# Function to start the server
def start_server():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    server = websockets.serve(audio_server, "localhost", 6789)  # Set WebSocket to localhost:6789
    print("WebSocket server started at ws://localhost:6789")
    loop.run_until_complete(server)
    loop.run_forever()

# Function to send data to all connected clients
async def broadcast(low_band=50, mid_band=50, high_band=50):
    if (debug): print(f"BROADCASTING: Low: {low_band}, Mid: {mid_band}, High: {high_band}")
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        await send_audio_data(websocket, low_band, mid_band, high_band)
        if (debug): print("Data sent to WebSocket server")
