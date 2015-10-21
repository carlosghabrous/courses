import numpy as np
import sys, os, math
from scipy.fftpack import fft

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../software/models/'))

import utilFunctions as UF

M = 501
hM1 = int( math.floor( (M + 1)/2 ) )
hM2 = int( math.floor( M/2 ) )

(fs, x) = UF.wavread('../sounds/soprano-E4.wav')
x1 = x[5000 : 5000 + M] * np.hamming(M)

N = 1024
fftbuffer = np.zeros(N)
fftbuffer[:hM1] = x1[hM2:]
fftbuffer[N-hM2:] = x1[:hM2]

X = fft(fftbuffer)
mX = 20 * np.log10( abs(X) )
pX = np.unwrap( np.angle(X) )