import sys, time
bar = ["[",".",".",".",".",".",".",".",".","]"]

def showbar():
 for i in bar:
  print (i, end="")
 print ()

def loading(x):

 if bar[x] == ".":
  bar[x] = "█"
  time.sleep(0.1)

 if bar[x] == bar[-1]:
  print ("100%")
  sys.exit()

 AI(x)

def AI(x):
 showbar()
 loading(x+1)

AI(0)
