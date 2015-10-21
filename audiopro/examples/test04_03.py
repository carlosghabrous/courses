import os, sys
sys.path.append( os.path.join( os.path.dirname( os.path.realpath(__file__) ), '../sms-tools/software/models/' ) )
import utilFunctions as UF
import stft as STFT

from scipy.signal import get_window

inputFile = '../sms-tools/sounds/flute-A4.wav'
window = 'hamming'

M = 801
N = 1024
H = 400

(fs, x) = UF.wavread(inputFile)

w = get_window(window, M)

(s_mX, s_pX) = STFT.stftAnal(x, fs, w, N, H)