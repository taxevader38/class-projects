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
import core.rideshare_calc_system as rideshare_calc_system

#Run the main program
def main():
    rideshare_calc_system.main()

#Ensure the main program only runs when this file is executed directly
if __name__ == "__main__":
    main()
