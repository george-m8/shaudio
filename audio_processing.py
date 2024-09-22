# audio_processing.py
import numpy as np

debug = True

# Function to process the audio data
def process_audio(audio_data):

    # Calculate RMS (volume)
    rms = np.sqrt(np.mean(np.square(audio_data)))
    
    # Perform FFT (for frequency analysis)
    fft_magnitude = np.abs(np.fft.rfft(audio_data))
    
    # Example: Calculate frequency band levels (e.g., low, mid, high)
    low_band = fft_magnitude[0:20].mean()   # 0-20Hz
    mid_band = fft_magnitude[21:200].mean()  # 21-200Hz
    high_band = fft_magnitude[201:].mean()   # 201Hz+

    # Print the values or send them somewhere in your project
    if (debug): print(f"RMS: {rms}, Low: {low_band}, Mid: {mid_band}, High: {high_band}")

    return rms, low_band, mid_band, high_band
