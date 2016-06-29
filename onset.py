import librosa
import matplotlib.pyplot as plt
import numpy as np 

audio_file = '/audio_analysis/output_mp3/256bits/1.mp3'

y, sr = librosa.core.load(audio_file, sr=22050)
onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
o_env = librosa.onset.onset_strength(y, sr=sr)
onset_frames = librosa.onset.onset_detect(onset_envelope=o_env, sr=sr)

D=np.abs(librosa.stft(y))**2
print "********************",plt.figure()
print "2"
plt.subplot(2,1,1)
librosa.display.specshow(librosa.logamplitude(D, ref_power=np.max),x_axis='time', y_axis='log')
plt.title('Power spectrogram')
print "plotted ggraph "
plt.subplot(2, 1, 2)
plt.plot(o_env, label='Onset strength')
plt.vlines(onset_frames, 0, o_env.max(), color='r', alpha=0.9, linestyle='--', label='Onsets')
plt.xticks([])
plt.axis('tight')
plt.legend(frameon=True, framealpha=0.75)
print "Done"
plt.show()
plt.savefig("img.png")

