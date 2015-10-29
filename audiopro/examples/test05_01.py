import numpy as np
import matplotlib.pyplot as plt
import sys, os

from scipy.signal import get_window

sys.path.append( os.path.join(os.path.dirname(os.path.realpath(__file__)), '../sms-tools/software/models/') )
import dftModel as DFT
import utilFunctions as UF

(fs, x) = UF.wavread('../sms-tools/sounds/sine-440.wav')

M = 501
N = 512
t = -20

w = get_window('hamming', M)
x1 = x[.8*fs : .8*fs + M]
mX, pX = DFT.dftAnal(x1, w, N)

ploc = UF.peakDetection(mX, t)
iploc, ipmag, ipphase = UF.peakInterp(mX, pX, ploc)

freqaxis = fs * np.arange(N/2) / float(N)
plt.plot(freqaxis, mX[0:N/2])
plt.plot(fs * iploc / float(N), ipmag, marker='x', linestyle='')

plt.show()

