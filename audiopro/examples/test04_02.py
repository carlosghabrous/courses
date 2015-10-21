import math, sys
import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import get_window
from scipy.fftpack import fft

sys.path.append('../sms-tools/software/models/')
import dftModel as DFT



fs = 44100
f0 = 5000.0
M = 101

x = np.cos(2 * np.pi * f0 * np.arange(M)/float(fs))
N = 512
w = get_window('hamming', M)
mX, pX = DFT.dftAnal(x, w, N)

xaxis = np.arange(0, fs/2, fs/float(N))

plt.plot( xaxis, mX-max(mX) )
plt.show()