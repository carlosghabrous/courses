import matplotlib.pyplot as plt
import numpy as np


k = 5
N = 32 
n = np.arange(-N/2, N/2, 1)

s = np.exp(1j * 2 * np.pi * k * n / N)

plt.plot(n, np.imag(s))
plt.axis([-N/2, N/2 - 1, -1, 1])
plt.xlabel('samples')
plt.ylabel('Real component amplitude')
plt.show()