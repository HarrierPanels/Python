#!/bin/env python3

import time, sys #, emoji
lst = list(input("Enter elements: ").replace(" ", ""))

j = 1
while j <= len(lst):
	for i in lst:
		print ("Argument",j,i)
		j += 1
def argsum():
	lst2 = []
	for i in range(0, len(lst)-1):
		lst2.append(int(lst[i]) + int(lst[i+1]))
	
	lst2.append(int(lst[0]) + int(lst[-1]))
	return lst2

def emu(load):
	frames = "/ | \\ -"
	j = 0
	while j < 35:
		print (frames[j % len(frames)], load, end='\r')
		j += 1	
		time.sleep(0.1)
emu("  Loading ...")	
print (argsum())

score=["-----"]
for i in score:
	if i == "-":
		i = ":star:"
		time.sleep(0.1)
	print (score)
