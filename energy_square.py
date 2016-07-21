import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile # get the api
import librosa
import math
from os import listdir

base_path_loud = "/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/loud/"
base_path_no_loud = "/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/no_loud/"


loud_audios = listdir('/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/loud')
no_loud_audios = listdir('/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/no_loud')

# i=0
for audio in loud_audios :
	# fs, data = wavfile.read(base_path_loud + audio) # load the data
	fs, data = librosa.load(base_path_loud+audio)
	# np.savetxt(str(audio)+".txt", data)
	absolute_value = np.absolute(data) # calculate absolute values of channels
	data_square = absolute_value**2
	# np.savetxt(str(audio)+".txt", data_square)
	mean_value = np.mean(data_square)
	print "Loud Audio value "+ str(audio)+ "  : ", mean_value 
	# i+=1

print "******************************************************************"
print "=================================================================="

# for audio in no_loud_audios:
# 	fs, data = wavfile.read(base_path_no_loud + audio) # load the data
# 	absolute_value = np.absolute(data) # calculate absolute values of channels
# 	data_square = absolute_value**2
# 	# np.savetxt(str(audio)+"no_loud.txt", data_square)
# 	mean_value = np.mean(data_square)
# 	print "No Loud Audio value "+ str(audio)+ "  : ", mean_value


# i=0
# while i < 2:
# 	print "**************fs**********", fs
# 	print "*************data***********", data.shape
# 	a = data.T[i] # this is a two channel soundtrack, I get the first track
# 	c = fft(a) # calculate fourier transform (complex numbers list)

# 	aw = librosa.A_weighting(c)

# 	magnitude = np.absolute(aw)

# 	# np.savetxt("magnitude.txt", magnitude)
# 	rms = librosa.feature.rmse(magnitude)

# 	divide_ref = rms/(np.max(data)*0.707)

# 	spl_db = np.log10(divide_ref)

# 	np.savetxt('spl_db'+str(i)+'.txt', spl_db)

# 	final_db = spl_db + 0.00002

# 	np.savetxt('final_db'+str(i)+'.txt', final_db)

# 	intensity = final_db * 330

# 	np.savetxt('intensity'+str(i)+'.txt', intensity)

# 	i+=1
