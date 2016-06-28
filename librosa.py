# Beat tracking example	
from __future__ import print_function
import librosa

# 1. Get the file path to the included audio example
filename = '/home/rishabh/Documents/iAugmentor/AudioAnalysis/audio/1mp4.mp3'
# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.core.load(filename, sr=22050)
'''
# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# 4. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

print('Saving output to beat_times.csv')
librosa.output.times_csv('beat_times.csv', beat_times)
'''