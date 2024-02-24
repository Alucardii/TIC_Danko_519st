import numpy as np
import matplotlib.pyplot as plt
from scipy import signal, fft

n = 500
Fs = 1000
F_max = 7

random_signal = np.random.normal(0, 10, n)

t = np.arange(n) / Fs

w = F_max / (Fs / 2)
parameters_filter = signal.butter(3, w, 'low', output='sos')

filtered_signal = signal.sosfiltfilt(parameters_filter, random_signal)

def plot_signal(time, signal, title):
    fig, ax = plt.subplots(figsize=(21/2.54, 14/2.54))
    ax.plot(time, signal, linewidth=1)
    ax.set_xlabel('Час (с)', fontsize=14)
    ax.set_ylabel('Амплітуда', fontsize=14)
    plt.title(title, fontsize=14)
    plt.savefig('./figures/' + title + '.png', dpi=600)
    plt.show()

plot_signal(t, filtered_signal, 'Фільтрований сигнал')

spectrum = np.abs(np.fft.fftshift(np.fft.fft(filtered_signal)))
freqs = np.fft.fftshift(np.fft.fftfreq(n, 1/Fs))
def plot_spectrum(freqs, spectrum, title):
    fig, ax = plt.subplots(figsize=(21/2.54, 14/2.54))
    ax.plot(freqs, spectrum, linewidth=1)
    ax.set_xlabel('Частота (Гц)', fontsize=14)
    ax.set_ylabel('Амплітуда', fontsize=14)
    plt.title(title, fontsize=14)
    plt.savefig('./figures/' + title + '.png', dpi=600)
    plt.show()

plot_spectrum(freqs, spectrum, 'Спектр сигналу')

plt.close('all')
