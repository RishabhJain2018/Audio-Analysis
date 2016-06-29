#!/bin/bash/
echo this is a shell script

python <<@@
import math
print 'hello from Python!'
a=math.sqrt(64)
print a
@@
