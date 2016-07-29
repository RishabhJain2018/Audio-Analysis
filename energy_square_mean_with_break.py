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

def loud_cal(filename):
	data, fs = librosa.load(filename)
	absolute_value = np.absolute(data, dtype='float64')
	data_square = absolute_value**2
	mean_value = np.mean(data_square)
	print "The average of 5  seconds is : ", mean_value
	return mean_value


os.chdir(base_path_loud)
for extension in extension_list:
	for aud in glob.glob(extension):
		file1.write("Audio Sample %s" %aud)
		file1.write("\n")
		song = AudioSegment.from_mp3(aud)
		t = song.duration_seconds
		print  "Time of Audio :" + str(aud)+ " : ",t
		t = int(t*1000)
		file1.write("time = %f " %t)
		file1.write("\n")
		l = np.array((0), dtype='float64')
		i = 0
		while(i<=t):
			if((i+5000) <= t):
				extract = song[i:i+5000]
				extract.export(path+"test"+str(i)+".mp3", format="mp3")
				mean_value = loud_cal(path+"test"+str(i)+".mp3")
				file1.write("The average of seconds is : %f" %mean_value)
				file1.write("\n")
				l = np.append(l, mean_value)
			elif ((i+5000) > t):
				extract = song[i:t]
				extract.export(path+"test"+str(i)+".mp3", format="mp3")
				mean_value = loud_cal(path+"test"+str(i)+".mp3")
				l = np.append(l, mean_value)
				file1.write("The average of seconds is : %f" %mean_value)
				file1.write("\n")
				break
			i+=5000
		final_mean = np.mean(l)
		compare_value1 = np.append(compare_value1, final_mean)
		mean_value1 = np.mean(compare_value1)
		file1.write("Final Mean of Loud audio : "+str(aud)+" : %f" %final_mean)
		file1.write("\n")
		print "Final Mean of Loud audio : "+str(aud)+" : ", final_mean
		print "\n"
file1.close()

os.chdir(base_path_no_loud)
for extension in extension_list:
	for aud in glob.glob(extension):
		file2.write("Audio Sample %s" %aud)
		file2.write("\n")
		song = AudioSegment.from_mp3(aud)
		t = song.duration_seconds
		print  "Time of Audio :" + str(aud)+ " : ",t
		t = int(t*1000)
		file2.write("time = %f " %t)
		file2.write("\n")
		l = np.array((0), dtype='float64')
		i = 0
		while(i<=t):
			if((i+5000) <= t):
				extract = song[i:i+5000]
				extract.export(path+"test"+str(i)+".mp3", format="mp3")
				mean_value = loud_cal(path+"test"+str(i)+".mp3")
				file2.write("The average of seconds is : %f" %mean_value)
				file2.write("\n")
				l = np.append(l, mean_value)
			elif ((i+5000) > t):
				extract = song[i:t]
				extract.export(path+"test"+str(i)+".mp3", format="mp3")
				mean_value = loud_cal(path+"test"+str(i)+".mp3")
				l = np.append(l, mean_value)
				file2.write("The average of seconds is : %f" %mean_value)
				file2.write("\n")
				break
			i+=5000
		final_mean = np.mean(l)
		compare_value2 = np.append(compare_value2, final_mean)
		mean_value2 = np.mean(compare_value2)
		file2.write("Final Mean of Loud audio : "+str(aud)+" : %f" %final_mean)
		file2.write("\n")
		print "Final Mean of Loud audio : "+str(aud)+" : ", final_mean
		print "\n"
file2.close()

final_compare_value = (mean_value1+mean_value2)/2
print "\n "
print "Final compare value is ", final_compare_value 
