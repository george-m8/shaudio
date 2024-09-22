# audio_effects.py
import numpy as np
from pydub import AudioSegment
from pydub.effects import normalize

def apply_effects(audio_data):
    """
    Apply audio effects like compression to the input audio.
    :param audio_data: A numpy array representing the raw audio input.
    :return: Processed audio data as a numpy array.
    """
    # Convert numpy array to AudioSegment for processing with pydub
    audio_segment = AudioSegment(
        data=audio_data.tobytes(),
        sample_width=audio_data.dtype.itemsize,
        frame_rate=44100,
        channels=1
    )
    
    # Apply compression or other effects (this example uses normalization)
    processed_audio_segment = normalize(audio_segment) # Is supposed to apply compressor like effect but is making massive numbers

    # Convert back to numpy array for further processing
    processed_audio = np.array(processed_audio_segment.get_array_of_samples()).astype(np.float32)

    return processed_audio