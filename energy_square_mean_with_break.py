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
		song = AudioSegment.from_mp3(aud)
		t = song.duration_seconds
		print  "Time of Audio :" + str(aud)+ " : ",t
		t = int(t*1000)
		l = np.array((0), dtype='float64')
		i = 0
		while(i<=t):
			if((i+5000) <= t):
				extract = song[i:i+5000]
				extract.export(path+"test"+str(i)+".mp3", format="mp3")
				l = np.append(l,loud_cal(path+"test"+str(i)+".mp3"))
			elif ((i+5000) > t):
				extract = song[i:t]
				extract.export(path+"test"+str(i)+".mp3", format="mp3")
				l = np.append(l,loud_cal(path+"test"+str(i)+".mp3"))
				break
			i+=5000
		final_mean = np.mean(l)
		print "\n"
		print "Final Mean of Loud audio : "+str(aud)+" : ", final_mean
		print "\n"

os.chdir(base_path_no_loud)
for extension in extension_list:
	for aud in glob.glob(extension):
		song = AudioSegment.from_mp3(aud)
		t = song.duration_seconds
		print  "Time of Audio :" + str(aud)+ " : ",t
		t = int(t*1000)
		l = np.array((0), dtype='float64')
		i = 0
		while(i<=t):
			if((i+5000) <= t):
				extract = song[i:i+5000]
				extract.export(path+"test"+str(i)+".mp3", format="mp3")
				l = np.append(l,loud_cal(path+"test"+str(i)+".mp3"))
			elif ((i+5000) > t):
				extract = song[i:t]
				extract.export(path+"test"+str(i)+".mp3", format="mp3")
				l = np.append(l,loud_cal(path+"test"+str(i)+".mp3"))
				break
			i+=5000
		final_mean = np.mean(l)
		print "\n"
		print "Final Mean of Not Loud audio : "+str(aud)+" : ", final_mean
