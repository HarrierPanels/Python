#####
from time import sleep
from tqdm import tqdm
for i in tqdm(range(10)):
    sleep(0.1)

#########
print ("\n")
#####
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
import sys
import time
loading= "LOADING\n"
bar = "[IIIIIIIIIIIIIIIIIIIIIIIIII]"
print(loading)
for c in bar:
    time.sleep(0.1)
    sys.stdout.write(c)
    sys.stdout.flush()
print ("\r")

##############
print ("\n")
##########
import time

import typer
from rich.progress import Progress, SpinnerColumn, TextColumn


def main():
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Processing...", total=None)
        progress.add_task(description="Preparing...", total=None)
        time.sleep(5)
    print("Done!")


if __name__ == "__main__":
    typer.run(main)

##############
print ("\n")
##########
print (st)
# Function to create 
def animated_marker():

    widgets = ['Loading: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()

    for i in range(50):
        time.sleep(0.1)
        bar.update(i)

# Driver's code
animated_marker()

