"""
Author: Christopher Bengen

Date: 1 / 05 / 26

Program Name: Ride Fare Calculator

Description: A program used to calculate the cost of a ride fare in the
             state of NJ
            
Extra: : Loading bar, tip option with different amounts, 
        receipt, try-except catching, input handling constrainting,
        and text effects

Citations:

Random Dictionary Pair Selection:
Title: How can I get a random key-value pair from a dictionary?
Author: tekknolagi
Date: Jan, 7 2026
Availability: https://stackoverflow.com/questions/4859292/how-can-i-get-a-random-key-value-pair-from-a-dictionary
"""

# =============== Imports ===============


from sfx.text import slowprint, color_text
from sfx.sfx import loading_bar
import random

dur = random.randint(1, 5)
step = random.randint(10, 50)

#Run the main program
def main_fare():
    rideshare_calc_system.main()

def main_binary_calc():
    binary_calc_system.main()

#Ensure the main program only runs when this file is executed directly
if __name__ == "__main__":
    slowprint("Available Programs In Directory:\n")
    print("1. Rideshare Fare Calculator")
    print("2. Binary Calculator\n")

    try:
        decision = input("Choose a program to run (1/2)\n > ")
    except (KeyboardInterrupt, EOFError):
        slowprint(color_text("\nWrong input type, try again", "red"), 0.03)

    while decision in ["1", "2"]:
        
        if decision == "1":
            loading_bar(dur, step)
            import fare_program.core.rideshare_calc_system as rideshare_calc_system
            main_fare()
            
        if decision == "2":
            loading_bar(dur, step)
            import binary_calc_program.core as binary_calc_system
            main_binary_calc()
            
