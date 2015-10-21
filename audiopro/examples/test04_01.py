import math
import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import get_window
from scipy.fftpack import fft


M = 63
window = get_window('blackmanharris', M)
hM1 = int ( math.floor( (M + 1)/2 ) )
hM2 = int ( math.floor( M/2 ) )

N = 512
fftbuffer = np.zeros(N)
fftbuffer[:hM1] = window[hM2:]
fftbuffer[N-hM2:] = window[:hM2]

X = fft(fftbuffer)
absX = abs(X)
absX[absX < np.finfo(float).eps] = np.finfo(float).eps
mX = 20 * np.log10(absX)
pX = np.angle(X)

mX1 = np.zeros(N)
pX1 = np.zeros(N)

mX1[:N/2] = mX[N/2:]
mX1[N/2:] = mX[:N/2]

pX1[:N/2] = pX[N/2:]
pX1[N/2:] = pX[:N/2]

plt.plot(np.arange(-N/2, N/2)/float(N)*M, mX1-max(mX1))
plt.axis([-20, 20, -120, 0])
plt.show()

