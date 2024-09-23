import asyncio
import websockets
import json

connected_clients = set()  # To keep track of all connected clients

# Function to broadcast the audio data to all connected clients
async def broadcast(low, mid, high):
    if connected_clients:  # Check if there are clients connected
        print(f"Broadcasting to {len(connected_clients)} clients")  # Debug: number of connected clients
        data = {
            "low": float(low),  # Convert to float
            "mid": float(mid),  # Convert to float
            "high": float(high)  # Convert to float
        }
        message = json.dumps(data)  # Convert to JSON string

        print(f"Broadcasting message: {message}")  # Debug: show the message being broadcasted

        # Create tasks for each coroutine and run them explicitly
        tasks = [asyncio.create_task(client.send(message)) for client in connected_clients]
        try:
            await asyncio.gather(*tasks)  # Await the completion of all tasks
            print("Broadcast successful")  # Debug: successful broadcast
        except Exception as e:
            print(f"Error during broadcast: {e}")  # Debug: any errors during broadcasting
    else:
        print("No clients connected. Skipping broadcast.")  # Debug: no clients connected

# WebSocket handler
async def websocket_handler(websocket, path):
    # Register client
    print("New client connected")  # Debug: new client connection
    connected_clients.add(websocket)
    try:
        async for _ in websocket:  # Just keep the connection alive
            pass
    except Exception as e:
        print(f"Error with client connection: {e}")  # Debug: any errors with the connection
    finally:
        # Unregister client
        connected_clients.remove(websocket)
        print("Client disconnected")  # Debug: client disconnect

# Function to start the WebSocket server
async def start_websocket_server():
    async with websockets.serve(websocket_handler, "localhost", 6789):
        print("WebSocket server started on ws://localhost:6789")  # Debug: server started
        await asyncio.Future()  # Run the server forever
