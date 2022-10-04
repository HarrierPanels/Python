#!/bin/env python3

import time, sys
score=list("----")
print (score)
for i in score:
	if i == "-":
		i = ":star:"
		time.sleep(0.1)
		while len(i) < len(score):
			print (score[i % len(score)], end="\r")
print (score, end="\r" "\n")
