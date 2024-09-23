# audio_input.py
import sounddevice as sd
import numpy as np
import asyncio

from audio_websocket import broadcast
from audio_effects import apply_effects
from audio_processing import process_audio  # Import the processing function

debug = False

# Get the running event loop (will be set in main.py)
loop = None

# Callback to capture audio
def audio_callback(indata, frames, time, status):
    global loop

    if status:
        print(status)
    
    audio_data = indata.flatten()  # Flatten the audio data to 1D array

    #audio_data = apply_effects(audio_data) # Is supposed to apply compressor like effect but is making massive numbers
    
    # Send audio data to the processor for analysis
    rms, low_band, mid_band, high_band = process_audio(audio_data)

    if (debug): print (f"audio_input: RMS: {rms}, Low: {low_band}, Mid: {mid_band}, High: {high_band}")

    # Use the global event loop to broadcast the audio bands asynchronously
    asyncio.run_coroutine_threadsafe(broadcast(low_band, mid_band, high_band), loop)

def start_audio_stream():
    # Start the audio input stream
    with sd.InputStream(callback=audio_callback, channels=1, samplerate=44100):
        print("Recording... Press Ctrl+C to stop.")
        while True:
            pass
