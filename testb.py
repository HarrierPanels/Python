#####
def tqtmbar():
 from time import sleep
 from tqdm import tqdm
 for i in tqdm(range(10)):
    sleep(0.1)

#########
print ("\n")
#####
def tqtmbar2():
 from tqdm import tqdm
 import time
 for i in tqdm (range (101), 
               desc="Loading…", 
               ascii=False, ncols=75):
    time.sleep(0.01)
      
 print("Complete.")

######
print ("\n")
##########
def progbar():
 import progressbar
 import time
 # Function to create 
 def animated_marker():
      
    widgets = ['Loading: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
      
    for i in range(50):
        time.sleep(0.1)
        bar.update(i)
          
 # Driver's code
 animated_marker()


##########
print ("Super\n")
###############
def simplebar(loading,bar):
 import sys, time
# bar = ": ███████████████████████████████████ 100%"
 print(loading)
 for c in bar:
    time.sleep(0.1)
    sys.stdout.write(c)
    sys.stdout.flush()
 print ("\r")

##############
print ("\n")
##########
def superbar():
 import sys
 def progressbar(it, prefix="", size=60, out=sys.stdout): # Python3.3+
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print("{}[{}{}] {}/{}".format(prefix, "█"*x, "."*(size-x), j, count), 
                end='\r', file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)

 import time    
 for i in progressbar(range(25), "Computing: ", 40):
    time.sleep(0.1) # any code you need

##############
print ("\n")
##########
def loading():
 import progressbar
 import time
  
  
 # Function to create 
 def animated_marker():
      
    widgets = ['Loading: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
      
    for i in range(50):
        time.sleep(0.1)
        bar.update(i)
          
 # Driver's code
 animated_marker()
############
simplebar("Fuck","####")
#superbar()

