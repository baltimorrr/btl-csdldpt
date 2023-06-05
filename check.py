
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





# import numpy as np
# import scipy.io.wavfile as wav

# def calculate_low_energy(signal, window_size, threshold):
#     energy = np.sum(signal ** 2)  # Tính năng lượng tổng của toàn bộ tín hiệu
#     low_energy_frames = []

#     num_frames = len(signal) // window_size  # Số lượng khung hình trong tín hiệu

#     for i in range(num_frames):
#         start = i * window_size
#         end = start + window_size
#         frame = signal[start:end]
#         frame_energy = np.sum(frame ** 2)  # Tính năng lượng của từng khung hình

#         if frame_energy / energy < threshold:
#             low_energy_frames.append(frame)

#     return low_energy_frames

# # Đọc tệp âm thanh
# sample_rate, signal = wav.read("audio_file.wav")

# # Chuyển đổi tín hiệu thành dạng số thực và chuẩn hóa
# signal = signal.astype(np.float32) / 32767.0

# # Cấu hình các thông số
# window_size = 1024  # Kích thước của mỗi khung hình
# threshold = 0.1  # Ngưỡng năng lượng thấp

# # Tính toán low energy frames
# low_energy_frames = calculate_low_energy(signal, window_size, threshold)

# print("Low Energy Frames:", low_energy_frames)