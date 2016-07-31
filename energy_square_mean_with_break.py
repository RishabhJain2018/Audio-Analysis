import numpy as np 
from scipy.fftpack import fft
from scipy.io import wavfile
import librosa
import math
from os import listdir
import matplotlib.pyplot as plt
from pydub import AudioSegment
import glob
import os

base_path_loud = "/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/loud5/mp3/"
base_path_no_loud = "/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/no_loud4/mp3/"
path = "/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/segment_audio/"

extension_list = ('*.mp3', '*.wav')

file1 =open('/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/results/result_file_loud.csv', 'w')
file2 = open('/home/rishabh/Documents/iAugmentor/AudioAnalysis/scripts/results/result_file_not_loud.csv', 'w')

compare_value1 = np.array((0), dtype="float64")
compare_value2 = np.array((0), dtype="float64")

loud_audios = listdir(base_path_loud)
not_loud_audios = listdir(base_path_no_loud)

def moving_average(a, n=3) :
	ret = np.cumsum(a, dtype=float)
	ret[n:] = ret[n:] - ret[:-n]
	return ret[n - 1:] / n

t_chunks = 5

def loud_cal(filename):
	final_mean = np.array((0), dtype='float64')
	y, sr = librosa.load(filename)
	y = np.absolute(y, dtype='float64')
	y = moving_average(y, 1000)
	# y /= np.min(y)
	off = np.mean(y[-1000:]**2)
	for i in range(0, len(y), sr*t_chunks):
		absolute_value = np.absolute(y[i:i+sr*t_chunks])
		data_square = absolute_value**2
		mean_value = np.mean(data_square)-off
		# print "mean value for chunk of 5 seconds : " , mean_value
		final_mean = np.append(final_mean, mean_value)
	# print "The average of 5  seconds is : ", mean_value
	final_mean_value = np.mean(final_mean)
	return final_mean_value

os.chdir(base_path_loud)
for extension in extension_list:
	for aud in glob.glob(extension):
		a = loud_cal(aud)
		print "Loud audio value for complete audio is : " +str(aud)+" : ", loud_cal(aud)
		print "\n"
		compare_value1 = np.append(compare_value1, a)

print "********************************************************************************"
print "********************************************************************************"

os.chdir(base_path_no_loud)
for extension in extension_list:
	for aud in glob.glob(extension):
		b = loud_cal(aud)
		print "Not Loud audio value for complete audio is : " +str(aud)+" : ", loud_cal(aud)
		print "\n"
		compare_value2 = np.append(compare_value2, b)


final_compare_value = (np.mean(compare_value1)+np.mean(compare_value2))/2
print "\n "
print "Final compare value is ", final_compare_value 

# file1.write("Audio Sample %s" %aud)
# file1.write("\n")
# song = AudioSegment.from_mp3(aud)
# 		t = song.duration_seconds
# 		# print  "Time of Audio :" + str(aud)+ " : ",t
# 		t = int(t*1000)
# 		# file1.write("time = %f " %t)
# 		# file1.write("\n")
# 		l = np.array((0), dtype='float64')
# 		i = 0
# 		while(i<=t):
# 			if((i+5000) <= t):
# 				extract = song[i:i+5000]
# 				extract.export(path+"test"+str(i)+".mp3", format="mp3")
# 				mean_value = loud_cal(path+"test"+str(i)+".mp3")
# 				# file1.write("The average of 5 seconds is : %f" %mean_value)
# 				# file1.write("\n")
# 				l = np.append(l, mean_value)
# 			elif ((i+5000) > t):
# 				extract = song[i:t]
# 				extract.export(path+"test"+str(i)+".mp3", format="mp3")
# 				mean_value = loud_cal(path+"test"+str(i)+".mp3")
# 				l = np.append(l, mean_value)
# 				# file1.write("The average of 5 seconds is : %f" %mean_value)
# 				# file1.write("\n")
# 				break
# 			i+=5000
# 		final_mean = np.mean(l)
# 		compare_value1 = np.append(compare_value1, final_mean)
# 		mean_value1 = np.mean(compare_value1)
# 		file1.write("Final Mean of Loud audio : "+str(aud)+" : %f" %final_mean)
# 		file1.write("\n")
# 		print "Final Mean of Loud audio : "+str(aud)+" : ", final_mean
# print "Mean value of Loud Audios : ", mean_value1
# file1.close()

# os.chdir(base_path_no_loud)
# for extension in extension_list:
# 	for aud in glob.glob(extension):
# 		# file2.write("Audio Sample %s" %aud)
# 		# file2.write("\n")
# 		song = AudioSegment.from_mp3(aud)
# 		t = song.duration_seconds
# 		# print  "Time of Audio :" + str(aud)+ " : ",t
# 		t = int(t*1000)
# 		# file2.write("time = %f " %t)
# 		# file2.write("\n")
# 		l = np.array((0), dtype='float64')
# 		i = 0
# 		while(i<=t):
# 			if((i+5000) <= t):
# 				extract = song[i:i+5000]
# 				extract.export(path+"test"+str(i)+".mp3", format="mp3")
# 				mean_value = loud_cal(path+"test"+str(i)+".mp3")
# 				# file2.write("The average of 5 seconds is : %f" %mean_value)
# 				# file2.write("\n")
# 				l = np.append(l, mean_value)
# 			elif ((i+5000) > t):
# 				extract = song[i:t]
# 				extract.export(path+"test"+str(i)+".mp3", format="mp3")
# 				mean_value = loud_cal(path+"test"+str(i)+".mp3")
# 				l = np.append(l, mean_value)
# 				# file2.write("The average of 5 seconds is : %f" %mean_value)
# 				# file2.write("\n")
# 				break
# 			i+=5000
# 		final_mean = np.mean(l)
# 		compare_value2 = np.append(compare_value2, final_mean)
# 		mean_value2 = np.mean(compare_value2)
# 		file2.write("Final Mean of Loud audio : "+str(aud)+" : %f" %final_mean)
# 		file2.write("\n")
# 		print "Final Mean of Not Loud audio : "+str(aud)+" : ", final_mean
# print "Mean value of Non Loud Audios : ", mean_value2
# file2.close()
