# =============== Imports ===============
import sys
import random
import time
from core.text import slowprint, color_text 
from core.calculation import fare_calc, tip

# =============== Global Variables ===============
#Flag for while loop
active_drive = False

# =============== Function Definitions ===============
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

def receipt(fare, tip_amount=0, total=0):
    """
    Print a receipt with the fare, tip, and total cost for the ride
    """

    #Get the total amount of money from the ride
    total = fare + tip_amount
    print("\n----- Receipt -----")

    #Print the fare, tip (if applicable), and total cost of the ride
    print(f"Fare: ${fare:.2f}")
    if tip_amount > 0:
        print(f"Tip: ${tip_amount:.2f}")
    print(f"Total: ${total:.2f}")
    print("-------------------")

# =============== Main Program ===============
#Random duration and step count for variability with the loading bar
dur = random.randint(1, 5)
step = random.randint(10, 50)

try:
    set_drive = input("Do you want to go for a drive? (y/n)\n > ")
except (KeyboardInterrupt, EOFError):
    slowprint("\nNot sure thats something you can say or do, rude", 0.03)
    
if set_drive == "y":
    active_drive = True
elif set_drive == "n":
    slowprint("\nThats fine, have a great day!", 0.03)
else:
    slowprint("\nNot sure thats something you can say or do, rude", 0.03)

#While loop to prevent user from hitting enter to not input anything
while active_drive:
    #Prevent users from entering values that are not numeric
    try:
        km = float(input("\nHow far do you want to travel? (km)\n > "))
    except (ValueError, KeyboardInterrupt, EOFError):
        slowprint(color_text("\n- Use an actual distance", "red"), 0.03)
        continue
    
    slowprint("Calculating cost\n", 0.03)
    
    loading_bar(dur, step)
    
    fare = fare_calc(km)
    slowprint(color_text(f"\nYour total is: ${fare:.2f}", "green"), 0.03)
    
    slowprint("\nWould you like to tip? (y/n)", 0.03)
    
    try:
        choice = input("> ").lower().strip()
    except (KeyboardInterrupt, EOFError):
        slowprint(color_text("\nIncorrect input, try again", "red"), 0.03)
        continue
    
    if choice not in ['y', 'n']: 
        slowprint(color_text("\nIncorrect input, restart ride order", "red"), 0.03)
        continue
    while choice in ['y', 'n']:
        if choice == 'y':
            tip_num = tip(fare)
            total = fare + tip_num
            slowprint(f"\nYour new total is: ${total:.2f}\n", 0.03)
            break
        else:
            if choice == 'n':
                slowprint("\nNo tip added.\n", 0.03)
                break
            
    loading_bar(dur, step)
    receipt(fare, tip_num if choice == 'y' else 0, total if choice == 'y' else fare)
    break