import numpy as np
import matplotlib.pyplot as plt


import sys, os
sys.path.append( os.path.join(os.path.dirname(os.path.realpath(__file__)), '../sms-tools/software/models/') )

from scipy.signal import get_window, blackmanharris, triang
from scipy.fftpack import ifft
from math import ceil

import dftModel as DFT
import utilFunctions as UF

# constants
window = 'blackman'
t = -40

# input
fileName = '../sms-tools/sounds/sine-200.wav'
f = 200.0


fs, x = UF.wavread(fileName)


#inside loop

k = 1
while True:

	M = 100 * k + 1
	N = 2**( int ( ceil( np.log2(M)) ) )

	w = get_window(window, M)
	x1 = x[.5*fs : .5*fs + M]
	mX, pX = DFT.dftAnal(x1, w, N)

	peak = UF.peakDetection(mX, t)
	ippeak, ipmag, ipphase = UF.peakInterp(mX, pX, peak)
	ippeak_Hz = ippeak * fs / float(N)
	f_error = abs(ippeak_Hz - f)


	if f_error.size > 0: 
		print 'k %d, M %d, N %d, error: %f' % (k, M, N, f_error[0])
		if f_error[0] < 0.05:
			break

	k += 1


#return (fEst, M, N)

