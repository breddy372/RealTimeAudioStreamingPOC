import numpy as np

def calculate_rms(audio_data):
    """Calculate the root mean square (RMS) of the audio data."""
    return np.sqrt(np.mean(np.square(audio_data)))

def trim_silence(audio_data, threshold=0.01):
    """Trim leading and trailing silence from audio data."""
    abs_data = np.abs(audio_data)
    start = np.argmax(abs_data > threshold)
    end = len(abs_data) - np.argmax(abs_data[::-1] > threshold)
    return audio_data[start:end]