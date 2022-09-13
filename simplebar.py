def simplebar(loading,bar):
 import time, sys
 print (loading)
 for i in bar:
  time.sleep(0.1)
  sys.stdout.write(i)
  sys.stdout.flush()
 print ("\n")
