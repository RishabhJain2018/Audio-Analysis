# import librosa

# filename =  "1.mp4"
# y, sr = librosa.load(filename)

# fft_freq = librosa.core.fft_frequencies()


import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile # get the api
fs, data = wavfile.read('1.wav') # load the data
import librosa


print "**************fs**********", fs
print "*************data***********", data.shape
a = data.T[0] # this is a two channel soundtrack, I get the first track
c = fft(a) # calculate fourier transform (complex numbers list)
# d = len(c)/2  # you only need half of the fft list (real signal symmetry)
# np.savetxt('c.txt', c)
# print "**************/*a*************", c.shape
aw = librosa.A_weighting(c)
# np.savetxt('aw.txt', aw)
for i in aw:
	magnitude = np.sqrt(i[0]**2 + i[1]**2)
	np.savetxt('magnitude.txt', magnitude)







# b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
# plt.plot(abs(c[:(d-1)]),'r') 
# plt.show()
