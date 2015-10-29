import numpy as np
import matplotlib.pyplot as plt
import sys, os

from scipy.signal import get_window

sys.path.append( os.path.join(os.path.dirname(os.path.realpath(__file__)), '../sms-tools/software/models/') )
import dftModel as DFT
import utilFunctions as UF

bins = np.array([-4, -3, -2, -1, 0, 1, 2, 3])
X = UF.genBhLobe(bins)