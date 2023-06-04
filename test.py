# import librosa

# # Load the audio file
# audio_file = 'D:\Quy\HCSDLDPT\dontau\danbau.wav'
# y, sr = librosa.load(audio_file)

# # Calculate the spectral centroid
# spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]

# # Print the spectral centroids
# print("Spectral centroids:", spectral_centroids)




# import numpy as np
# import scipy.io.wavfile as wav

# # Đọc file âm thanh và lấy dữ liệu
# sample_rate, data = wav.read("D:\Quy\HCSDLDPT\dontau\danbau.wav")

# # Chuyển đổi dữ liệu âm thanh sang dạng số phức
# data = np.fft.fft(data)

# # Tính tần số của mỗi mẫu trong FFT
# freqs = np.fft.fftfreq(len(data))

# # Lấy giá trị tuyệt đối và chuẩn hóa mảng dữ liệu
# magnitudes = np.abs(data)
# magnitudes /= np.sum(magnitudes)

# # Tính Spectral Centroid
# centroid = np.sum(freqs * magnitudes)

# print("Spectral Centroid:", centroid)


# import numpy as np
# import scipy.io.wavfile as wav
# from scipy.signal import spectrogram

# # Đọc file âm thanh và lấy dữ liệu
# sample_rate, data = wav.read("D:\Quy\HCSDLDPT\dontau\danbau.wav")

# # Tính phổ âm thanh
# frequencies, times, spectrogram_data = spectrogram(data, sample_rate)

# # Chuẩn hóa phổ âm thanh
# spectrogram_data /= np.sum(spectrogram_data)

# # Tính Spectral Centroid
# centroid = np.sum(frequencies * spectrogram_data, axis=0) / np.sum(spectrogram_data, axis=0)

# print("Spectral Centroid:", centroid)


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
# sample_rate, signal = wav.read("D:\Quy\HCSDLDPT\dontau\danbau.wav")

# # Chuyển đổi tín hiệu thành dạng số thực và chuẩn hóa
# signal = signal.astype(np.float32) / 32767.0

# # Cấu hình các thông số
# window_size = 1024  # Kích thước của mỗi khung hình
# threshold = 0.1  # Ngưỡng năng lượng thấp

# # Tính toán low energy frames
# low_energy_frames = calculate_low_energy(signal, window_size, threshold)

# print("Low Energy Frames:", low_energy_frames)


import numpy as np
import scipy.io.wavfile as wav
from scipy.signal import spectrogram

# Đọc file âm thanh và lấy dữ liệu
sample_rate, data = wav.read("D:\Quy\HCSDLDPT\dontau\danbau.wav")

# Tính phổ âm thanh
frequencies, times, spectrogram_data = spectrogram(data, sample_rate, nperseg=len(data))

# Chuẩn hóa phổ âm thanh
spectrogram_data /= np.sum(spectrogram_data)

# Tính Spectral Centroid
centroid = np.sum(frequencies * spectrogram_data, axis=0) / np.sum(spectrogram_data, axis=0)

print("Spectral Centroid:", centroid)















