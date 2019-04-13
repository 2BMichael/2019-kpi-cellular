import numpy as np
from scipy.io import wavfile

fs = 44100

f1 = int(300)
f2 = int(600)
t = float(120)

samples = np.arange(t * fs) / fs

signal1 = np.sin(2 * np.pi * f1 * samples)

signal2 = np.sin(2 * np.pi * f2 * samples)
signal = signal1 + signal2
wavfile.write('task1', fs, signal)
