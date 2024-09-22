# audio_stream.py
import pyaudio
import numpy as np

class AudioStream:
    def __init__(self, rate=44100, channels=1, format=pyaudio.paInt16, frames_per_buffer=1024):
        self.rate = rate
        self.channels = channels
        self.format = format
        self.frames_per_buffer = frames_per_buffer
        
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.format,
                                  channels=self.channels,
                                  rate=self.rate,
                                  input=True,
                                  frames_per_buffer=self.frames_per_buffer)

    def read_audio(self):
        data = self.stream.read(self.frames_per_buffer)
        audio_data = np.frombuffer(data, dtype=np.int16)
        return audio_data

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    def is_working(self):
        return self.p.is_format_supported(self.rate, input_device=0, input_channels=self.channels, input_format=self.format)
