import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile # get the api
import librosa
import math
from os import listdir
# import matplotlib.pyplot as plt

base_path_loud = "/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/loud5/mp3/"
base_path_no_loud = "/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/no_loud4/mp3/"

file1 =open('/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/results/result_file_loud_without_break.csv', 'w')
file2 = open('/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/results/result_file_not_loud_without_break.csv', 'w')

loud_audios = listdir('/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/loud5/mp3')
no_loud_audios = listdir('/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/no_loud4/mp3')

def moving_average(a, n=3) :
	ret = np.cumsum(a, dtype=float)
	ret[n:] = ret[n:] - ret[:-n]
	return ret[n - 1:] / n

average_values1 = np.array((0), dtype='float64')
for audio in loud_audios :
	data, fs = librosa.load(base_path_loud+audio)
	data = moving_average(data, 1000)
	absolute_value = np.absolute(data, dtype='float64') # calculate absolute values of channels
	data_square = absolute_value**2
	mean_value = np.mean(data_square)
	print "Loud Audio value : "+ str(audio)+ "  : ", mean_value
	file1.write("Loud audio value :"+str(audio)+" : %f" %mean_value)
	file1.write("\n")
	average_values1 = np.append(average_values1, mean_value)

file1.close()
avg1 = np.mean(average_values1)
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

average_values2 = np.array((0,0), dtype='float64')
for audio in no_loud_audios:
	data, fs = librosa.load(base_path_no_loud+audio)
	data = moving_average(data, 1000)
	# fs, data = wavfile.read(base_path_no_loud + audio) # load the data
	absolute_value = np.absolute(data, dtype='float64') # calculate absolute values of channels
	data_square = np.square(absolute_value)
	# np.savetxt(str(audio)+"no_loud.txt", data_square)
	mean_value = np.mean(data_square)
	print "Not Loud Audio value  :"+ str(audio)+ "  : ", mean_value
	file2.write("Not Loud Audio value  :"+ str(audio)+ "  : %f" %mean_value)
	file2.write("\n")
	average_values2 = np.append(average_values2, mean_value)
	# print average_values
	# print average_values
file2.close()
avg2 = np.mean(average_values2)
print "============================================================"
print "The average of the not loud means is :", avg2
# plt.plot(data_square)
# plt.xlabel("Sampling Rate")
# plt.ylabel("Amplitude")
# plt.title("Not Loud"+str(audio))
# plt.show()
# plt.savefig(str(audio.split(".")[0]), format="jpeg")


# print "The values are"
# print "\n "
# print " Loud Audio \t \t Value \t \t Not Loud Audio \t \t Value"
# for i in range(loud_audios):
# 	print "\t", i
# for i in range(average_values1):
# 	print "\t \t ", 

final_value = (avg1+avg2)/2
print "\n"
print "******The average of loud and not loud menas is****************", final_value
