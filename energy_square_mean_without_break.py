import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile # get the api
import librosa
import math
from os import listdir
import matplotlib.pyplot as plt

base_path_loud = "/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/loud5/mp3/"
base_path_no_loud = "/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/no_loud4/mp3/"

file1 =open('/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/results/result_file_loud_without_break.csv', 'w')
file2 = open('/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/results/result_file_not_loud_without_break.csv', 'w')

loud_audios = listdir('/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/loud5/mp3')
no_loud_audios = listdir('/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/no_loud4/mp3')

average_values = np.array((0), dtype='float64')
for audio in loud_audios :
	data, fs = librosa.load(base_path_loud+audio)
	absolute_value = np.absolute(data, dtype='float64') # calculate absolute values of channels
	data_square = absolute_value**2
	mean_value = np.mean(data_square)
	print "Loud Audio value : "+ str(audio)+ "  : ", mean_value
	file1.write("Loud audio value :"+str(audio)+" : %f" %mean_value)
	file1.write("\n")
	average_values = np.append(average_values, mean_value)

file1.close()
avg1 = np.mean(average_values)
print "******************************************"
print "The average of all the loud means is : ",avg1 

# print "squared data datatype",data_square.dtype
# # print "mean data datatype", mean_value.dtype
# plt.plot(data_square)
# plt.xlabel("Sampling rate")
# plt.ylabel("Amplitude")
# plt.title("Loud Audio"+str(audio))
# plt.show()
# plt.savefig(str(audio.split(".")[0]), format="jpeg")
# print average_values
print "**********************************************************"
print "=========================================================="

average_values = np.array((0,0), dtype='float64')
for audio in no_loud_audios:
	data, fs = librosa.load(base_path_no_loud+audio)
	# fs, data = wavfile.read(base_path_no_loud + audio) # load the data
	absolute_value = np.absolute(data, dtype='float64') # calculate absolute values of channels
	data_square = np.square(absolute_value)
	# np.savetxt(str(audio)+"no_loud.txt", data_square)
	mean_value = np.mean(data_square)
	print "Not Loud Audio value  :"+ str(audio)+ "  : ", mean_value
	file2.write("Not Loud Audio value  :"+ str(audio)+ "  : %f" %mean_value)
	file2.write("\n")
	average_values = np.append(average_values, mean_value)
	# print average_values
	# print average_values
file2.close()
avg2 = np.mean(average_values)
print "============================================================"
print "The average of the not loud means is :", avg2
# plt.plot(data_square)
# plt.xlabel("Sampling Rate")
# plt.ylabel("Amplitude")
# plt.title("Not Loud"+str(audio))
# plt.show()
# plt.savefig(str(audio.split(".")[0]), format="jpeg")

final_value = (avg1+avg2)/2
print "\n"
print "******The average of loud and not loud menas is****************", final_value
