import numpy as np
import soundfile as sf

def read_audio(file_path):
    """Read an audio file and return the data and sample rate."""
    data, samplerate = sf.read(file_path)
    return data, samplerate

def write_audio(file_path, data, samplerate):
    """Write audio data to a file."""
    sf.write(file_path, data, samplerate)

def normalize_audio(audio_data):
    """Normalize audio data to the range [-1, 1]."""
    return audio_data / np.max(np.abs(audio_data))