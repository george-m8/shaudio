from audio_stream import AudioStream 
from audio_analyser import *

import numpy as np

def main():
    stream = AudioStream()
    analyzer = AudioAnalyzer()
    
    debug = True

    get_audio_level = True
    get_frequency_levels = False
    
    if stream.is_working():
        if (debug): print("PyAudio is working")
        
        # Stream and process audio
        try:
            while True:
                audio_data = stream.read_audio()
                # Apply some NumPy operations on the audio data
                # For example, calculate the RMS (Root Mean Square) value of the audio
                if get_audio_level:
                    volume = analyzer.get_volume(audio_data)
                    print("Volume:", volume)
        except KeyboardInterrupt:
            print("Stopping stream...")
        finally:
            stream.close()
    else:
        print("PyAudio is not working")

if __name__ == "__main__":
    main()
