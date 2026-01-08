import sys
import time

def loading_bar(duration, steps):
    """
    Print a loading bar that goes progressively from 0 to 100% to simulate loading
    """
    #Simulate animation with steps
    for i in range(steps + 1):
        
        
        perc_loaded = 100.0 * i / steps
        
        #Define the loading bar 
        bar = '■' * int(perc_loaded / 2) + '-' * int(50 - perc_loaded / 2)
        
        #Use sys to print the loading bar on one line
        sys.stdout.write('\r[%s] %.2f%%' % (bar, perc_loaded))
        sys.stdout.flush()
        time.sleep(duration / steps)
    sys.stdout.write("\n")