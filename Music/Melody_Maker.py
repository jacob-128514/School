# outputs a basic circle of fifths progression

import pyaudio
import random
import numpy as np

p = pyaudio.PyAudio()

volume = 0.5
fs = 44100
duration = 1

N = random.randint(1,12)

f1 = 340*(2**(N/12))
f2 = f1*(2**(4/12)) # Major third
f3 = f1*(2**(7/12)) # Perfect fifth
f4 = f1*(2**(11/12)) # Major seventh

stream = p.open(format = pyaudio.paFloat32,
                channels = 1,
                rate=fs,
                output=True)

for i in range(8):
    sample1 = (np.sin(2*np.pi*np.arange(fs*duration)*f1/fs)).astype(np.float32)
    sample2 = (np.sin(2*np.pi*np.arange(fs*duration)*f2/fs)).astype(np.float32)
    sample3 = (np.sin(2*np.pi*np.arange(fs*duration)*f3/fs)).astype(np.float32)
    sample4 = (np.sin(2*np.pi*np.arange(fs*duration)*f4/fs)).astype(np.float32)

    if i % 2 == 0:
        stream.write(volume*(sample1))
        stream.write(volume*(sample2))
        stream.write(volume*(sample3))
        stream.write(volume*(sample4))

        f1 = f1*(2**(5/12)) # Perfect cadence
        f2 = f1*(2**(4/12)) # Major third
        f3 = (f1/2)*(2**(7/12)) # Perfect fifth
        f4 = (f1/2)*(2**(11/12)) # Major seventh

    else:
        stream.write(volume*(sample3))
        stream.write(volume*(sample4))
        stream.write(volume*(sample1))
        stream.write(volume*(sample2))

        f1 = (f1/2)*(2**(5/12)) # Perfect cadence (down one octave)
        f2 = f1*(2**(4/12)) # Major third
        f3 = f1*(2**(7/12)) # Perfect fifth
        f4 = f1*(2**(11/12)) # Major seventh
