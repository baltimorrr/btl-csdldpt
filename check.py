
import numpy as np
import librosa

# Load audio file
audio_file = 'D:\Quy\HCSDLDPT\dontau\danbau.wav'
audio, sr = librosa.load(audio_file)

# Calculate energy of audio frames
frame_size = 2048
hop_size = 512
frame_length = int(frame_size / hop_size)
energy = librosa.feature.rms(y=audio, frame_length=frame_length, hop_length=hop_size)[0]

# Set energy threshold
energy_threshold = np.mean(energy) * 0.5

# Find low energy segments
low_energy_segments = np.where(energy < energy_threshold)[0]

# Print low energy segments
print("Low Energy Segments:", low_energy_segments)






import librosa

# Load audio file
audio_file = 'D:\Quy\HCSDLDPT\dontau\danbau.wav'
audio, sr = librosa.load(audio_file)

# Compute the spectral centroid
spectral_centroids = librosa.feature.spectral_centroid(y=audio, sr=sr)

# Print the resulting spectral centroids
print("Spectral Centroids:", spectral_centroids)