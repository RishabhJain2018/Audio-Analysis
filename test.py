import sys
import aubio

s=aubio.source(sys.argv[1], 0, 256)
while True:
	samples, read = s()
	print samples
	if read < 256:
		break
		