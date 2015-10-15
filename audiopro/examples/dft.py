import numpy as np
import matplotlib.pyplot as plt 


N = 64
k0 = 7

# INPUTS
#x = np.exp(1j * 2 * np.pi * k0 / N * np.arange(N))
x = np.cos(2 * np.pi * k0 / N * np.arange(N))

#plt.plot(np.arange(N), x)
#plt.show()

# AXIS
nv = np.arange(-N/2, N/2)
kv = np.arange(-N/2, N/2)

# OUTPUT (DFT)
X = np.array([])

for k in kv:
	
	s = np.exp(1j * 2 * np.pi * k / N * nv)

	X = np.append( X, sum(x * np.conjugate(s)) )


#plt.plot(kv, abs(X) )
#plt.axis([-N/2, N/2 - 1, 0, N + 1])
#plt.xlabel('Frequency')
#plt.ylabel('Spectrum magnitude')
#plt.show()


y = np.array([])

for n in nv:

	s = np.exp(1j * 2 * np.pi * n / N * kv)

	y = np.append( y, 1.0/N * sum(X * s) )

plt.plot(range(-N/2, N/2), y)
plt.axis([-N/2, N/2-1, -1, 1])
plt.show()

