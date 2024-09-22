import numpy as np

class AudioAnalyzer:
    def __init__(self, rate=44100, frames_per_buffer=1024, clip_limit=32767):
        self.rate = rate
        self.frames_per_buffer = frames_per_buffer
        self.clip_limit = clip_limit
        self.freq_bins = np.fft.rfftfreq(frames_per_buffer, 1.0/rate)

    def compute_fft(self, audio_data):
        # Convert audio data to float to avoid integer overflow
        audio_data = audio_data.astype(np.float32)

        # Clip audio data to prevent overflow
        audio_data = np.clip(audio_data, -self.clip_limit, self.clip_limit)
        
        # Perform FFT on the audio data
        fft_data = np.fft.rfft(audio_data)
        # Get magnitude (absolute value)
        magnitude = np.abs(fft_data)
        return magnitude

    def get_volume(self, audio_data):
        # Convert audio data to float
        audio_data = audio_data.astype(np.float32)

        # Clip audio data to prevent extreme values
        audio_data = np.clip(audio_data, -self.clip_limit, self.clip_limit)

        # Calculate the mean of the squared values
        mean_square = np.mean(audio_data**2)

        # Normalize the volume value
        normalized_volume = self.normalize(mean_square, 0, self.clip_limit ** 2)
        # Clip to ensure it stays within [0, 1]
        normalized_volume = np.clip(normalized_volume, 0, 1)
        return normalized_volume

    def get_frequency_band_levels(self, fft_magnitude):
        # Example frequency bands: low, mid, high (you can customize these)
        bands = {
            "low": (20, 250),
            "mid": (250, 2000),
            "high": (2000, 8000)
        }
        band_levels = {}
        
        for band, (low, high) in bands.items():
            # Get the indices corresponding to the frequency range
            indices = np.where((self.freq_bins >= low) & (self.freq_bins <= high))
            # Sum the magnitude of those frequencies
            band_level = np.mean(fft_magnitude[indices])
            # Normalize the frequency band level using the max magnitude of the FFT
            band_levels[band] = self.normalize(band_level, 0, np.max(fft_magnitude))
            # Clip to ensure the values stay within [0, 1]
            band_levels[band] = np.clip(band_levels[band], 0, 1)
        
        return band_levels

    def normalize(self, value, min_val, max_val):
        """
        Normalizes a value (or array) to a range between 0 and 1.
        
        Args:
            value: The value or array to normalize.
            min_val: The minimum possible value in the range.
            max_val: The maximum possible value in the range.
        
        Returns:
            A normalized value or array between 0 and 1.
        """
        # Protect against division by zero if min_val == max_val
        if max_val == min_val:
            return 0.0
        
        # Normalize to the range [0, 1]
        return (value - min_val) / (max_val - min_val)
