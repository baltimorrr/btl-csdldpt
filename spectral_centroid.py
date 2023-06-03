import numpy as np
import scipy.io.wavfile as wav


# spectral centroid
def calculate_spectral_centroid(signal, sample_rate):
    magnitudes = np.abs(np.fft.rfft(signal))  # Tính phổ Fourier của tín hiệu
    frequencies = np.fft.rfftfreq(len(signal), d=1.0/sample_rate)  # Tính các tần số tương ứng với phổ
    spectral_centroid = np.sum(frequencies * magnitudes) / np.sum(magnitudes)  # Tính spectral centroid
    return spectral_centroid

# Đọc tệp âm thanh
sample_rate, signal = wav.read("audio_file.wav")

# Chuyển đổi tín hiệu thành dạng số thực và chuẩn hóa
signal = signal.astype(np.float32) / 32767.0

# Tính toán spectral centroid
centroid = calculate_spectral_centroid(signal, sample_rate)

print("Spectral Centroid:", centroid)


#flux
import numpy as np
import scipy.io.wavfile as wav

def calculate_flux(signal):
    flux = np.zeros_like(signal)  # Khởi tạo mảng flux với kích thước tương tự như tín hiệu
    flux[0] = 0  # Giá trị flux của khung hình đầu tiên là 0

    for i in range(1, len(signal)):
        flux[i] = np.sum(np.abs(signal[i] - signal[i-1]))  # Tính độ khác biệt giữa hai khung hình liên tiếp

    return flux

# Đọc tệp âm thanh
sample_rate, signal = wav.read("audio_file.wav")

# Chuyển đổi tín hiệu thành dạng số thực và chuẩn hóa
signal = signal.astype(np.float32) / 32767.0

# Tính toán flux
flux = calculate_flux(signal)

print("Flux:", flux)




#Low-Energy
import numpy as np
import scipy.io.wavfile as wav

def calculate_low_energy(signal, window_size, threshold):
    energy = np.sum(signal ** 2)  # Tính năng lượng tổng của toàn bộ tín hiệu
    low_energy_frames = []

    num_frames = len(signal) // window_size  # Số lượng khung hình trong tín hiệu

    for i in range(num_frames):
        start = i * window_size
        end = start + window_size
        frame = signal[start:end]
        frame_energy = np.sum(frame ** 2)  # Tính năng lượng của từng khung hình

        if frame_energy / energy < threshold:
            low_energy_frames.append(frame)

    return low_energy_frames

# Đọc tệp âm thanh
sample_rate, signal = wav.read("audio_file.wav")

# Chuyển đổi tín hiệu thành dạng số thực và chuẩn hóa
signal = signal.astype(np.float32) / 32767.0

# Cấu hình các thông số
window_size = 1024  # Kích thước của mỗi khung hình
threshold = 0.1  # Ngưỡng năng lượng thấp

# Tính toán low energy frames
low_energy_frames = calculate_low_energy(signal, window_size, threshold)

print("Low Energy Frames:", low_energy_frames)



#Rolloff
import numpy as np
import scipy.io.wavfile as wav

def calculate_rolloff(signal, sample_rate, rolloff_percent):
    fft = np.fft.fft(signal)  # Tính phổ Fourier của tín hiệu
    frequencies = np.fft.fftfreq(len(signal), d=1.0/sample_rate)  # Tính các tần số tương ứng với phổ

    # Sắp xếp các phần tử của fft theo thứ tự tăng dần của tần số
    sorted_fft = np.sort(fft)
    rolloff_index = int((1 - rolloff_percent) * len(fft))  # Tính chỉ số ngưỡng Rolloff

    rolloff_frequency = np.abs(frequencies[np.argmax(sorted_fft[rolloff_index:])])

    return rolloff_frequency

# Đọc tệp âm thanh
sample_rate, signal = wav.read("audio_file.wav")

# Chuyển đổi tín hiệu thành dạng số thực và chuẩn hóa
signal = signal.astype(np.float32) / 32767.0

# Cấu hình các thông số
rolloff_percent = 0.85  # Phần trăm ngưỡng Rolloff

# Tính toán Rolloff
rolloff_frequency = calculate_rolloff(signal, sample_rate, rolloff_percent)

print("Rolloff Frequency:", rolloff_frequency)






