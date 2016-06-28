import librosa
import matplotlib.pyplot as plt
import numpy as np 

filename = '/home/rishabh/Documents/iAugmentor/test_data/audios/128bits/2.mp3'

y, sr = librosa.core.load(filename, sr=22050)
onset_frames = librosa.onset.onset_detect(y=y, sr=sr)

D=np.abs(librosa.stft(y))**2
plt.figure()
plt.subplot(2,1,1)
librosa.display.specshow(librosa.logamplitude(D, ref_power=np.max),x_axis='time', y_axis='log')
plt.title('Power spectrogram')
print "plotted Graph"