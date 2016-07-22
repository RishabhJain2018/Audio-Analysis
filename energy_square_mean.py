import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile # get the api
import librosa
import math
from os import listdir
import matplotlib.pyplot as plt

base_path_loud = "/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/loud5/"
base_path_no_loud = "/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/no_loud4/"


loud_audios = listdir('/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/loud5')
no_loud_audios = listdir('/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/no_loud4')

for audio in loud_audios :
	fs, data = librosa.read(base_path_loud+audio)
	fs, data = wavfile.read(base_path_loud+audio)
	# np.savetxt(str(audio)+".txt", data)
	absolute_value = np.absolute(data, dtype='float32') # calculate absolute values of channels
	data_square = absolute_value**2
	# np.savetxt(str(audio)+".txt", data_square)
	mean_value = np.mean(data_square)
	print "Loud Audio value : "+ str(audio)+ "  : ", mean_value
	# print "squared data datatype",data_square.dtype
	# # print "mean data datatype", mean_value.dtype
	# plt.plot(absolute_value)
	# plt.xlabel("Sampling rate")
	# plt.ylabel("Amplitude")
	# plt.title("Loud Audio"+str(audio))
	# plt.show()
	# plt.savefig(str(audio.split(".")[0]), format="jpeg")

print "**********************************************************"
print "=========================================================="


for audio in no_loud_audios:
	fs, data = librosa.read(base_path_no_loud+audio)
	fs, data = wavfile.read(base_path_no_loud + audio) # load the data
	absolute_value = np.absolute(data, dtype='float32') # calculate absolute values of channels
	data_square = np.square(absolute_value)
	# np.savetxt(str(audio)+"no_loud.txt", data_square)
	mean_value = np.mean(data_square)
	print "Not Loud Audio value  :"+ str(audio)+ "  : ", mean_value
	# plt.plot(absolute_value)
	# plt.xlabel("Sampling Rate")
	# plt.ylabel("Amplitude")
	# plt.title("Not Loud"+str(audio))
	# plt.show()
	# plt.savefig(str(audio.split(".")[0]), format="jpeg")
