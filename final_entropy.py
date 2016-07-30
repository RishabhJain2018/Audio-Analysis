import os
import glob
from pydub import AudioSegment
import librosa
import numpy as np
import scipy
from scipy.stats import norm
import matplotlib.pyplot as plt
import pylab as pl

path = "/home/rishabh/Documents/iAugmentor/AudioAnalysis/"
aud_dir = "/home/audio_analysis/3monotonous/"
extension_list = ('*.mp3', '*.wav')
f = open('/home/audio_analysis/csv_files/result_file_monoest1000.csv', 'w')

def moving_average(a, n=3) :
	ret = np.cumsum(a, dtype=float)
	ret[n:] = ret[n:] - ret[:-n]
	return ret[n - 1:] / n

os.chdir(aud_dir)
print avg_entropy.dtype
for extension in extension_list:
	for filename in glob.glob(extension):	
		t_chunk = 5 
		y, sr = librosa.load(filename)
		y = moving_average(y, 1000)
		entr = []
		for i in range(0, len(y), sr*t_chunk):
			y1 = np.abs(y[i:i+sr*t_chunk])
			y1 /= y1
			entopy = norm.entropy(y1)
			entr = np.append(entr, entropy)
	print filename + ":"
	print "entropy:",entr


		