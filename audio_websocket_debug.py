# Simplified WebSocket server that sends dummy data to all clients
import asyncio
import websockets
import json

# Function to send dummy audio data over WebSocket
async def send_dummy_data(websocket, path):
    print("Client connected")
    try:
        while True:
            # Dummy data for testing
            data = {
                "low": 50,
                "mid": 50,
                "high": 50
            }
            print(f"Sending dummy data: {data}")
            await websocket.send(json.dumps(data))  # Send data as a JSON object
            await asyncio.sleep(2)  # Send every 2 seconds
    except websockets.ConnectionClosed:
        print("Client disconnected")

# Function to start the WebSocket server
def start_server():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    server = websockets.serve(send_dummy_data, "localhost", 6789)
    print("WebSocket server started at ws://localhost:6789")
    loop.run_until_complete(server)
    loop.run_forever()
