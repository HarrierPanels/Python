#!/bin/env python3
import time, sys
def load(loading):
	import time, sys
	def bar(bar):
		for i in bar:
			time.sleep(0.1)
			sys.stdout.write(i)
			sys.stdout.flush()
	frames = "/ | \\ -"
	i = 0
	while i < 35:
		print (frames[i % len(frames)], bar(loading), end='\r')
		i += 1
		time.sleep(0.1)
#def bar(bar):
#	for a in bar:
#		time.sleep(0.1)
#		sys.stdout.write(a)
#		sys.stdout.flush()
load("fuck .......")



