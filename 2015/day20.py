import numpy as np

def setupArray(N):
	a = np.zeros(N, dtype=int)
	for i in range(N):
		j = i+1
		a[i:j*50:j] += j * 11
	return a

a = setupArray(3310000)
print(np.where(a >= 33100000))
