import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile # get the api
import librosa
import math

fs, data = wavfile.read('1.wav') # load the data

i=0
while i < 2:
	print "**************fs**********", fs
	print "*************data***********", data.shape
	a = data.T[i] # this is a two channel soundtrack, I get the first track
	c = fft(a) # calculate fourier transform (complex numbers list)

	aw = librosa.A_weighting(c)

	magnitude = np.absolute(aw)

	# np.savetxt("magnitude.txt", magnitude)
	rms = librosa.feature.rmse(magnitude)

	divide_ref = rms/(np.max(data)*0.707)

	spl_db = np.log10(divide_ref)

	np.savetxt('spl_db'+str(i)+'.txt', spl_db)

	final_db = spl_db + 0.00002

	np.savetxt('final_db'+str(i)+'.txt', final_db)

	intensity = final_db * 330

	np.savetxt('intensity'+str(i)+'.txt', intensity)

	i+=1
