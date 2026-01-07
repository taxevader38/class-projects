# =============== Imports ===============
from core.text import slowprint, color_text

#Base cost added immediately
base_fare = 4

#Additional cost added every 140m
additional = 0.25

def fare_calc(km) -> float:
    """
    Calculate the total cost of the ride, dependent on the distance of the drive
    Uses distance as kilometers
    """
    
    #Calculate the cost by converting km back into m adding an additional fee for every 140 m
    cost = base_fare + (additional * ((km * 1000)/140))
    return cost

def tip(cost) -> float:
    """
    Calculate and return the amount of tip dependent on the total cost of the ride
    """
    slowprint("\nChoose your amount for tip:", 0.03)
    
    #Use a dictionary to store percent values attached with how it'd appear in a string
    percent = {
        5: 0.05,
        10: 0.1,
        15:0.15,
        20: 0.2,
        25:0.25
    }

    print("5% / 10% / 15% / 20% / 25%")
    
    #Get the raw input from the user regarding the percentages
    try:
        raw_per = input("> ")
    except (KeyboardInterrupt, EOFError):
        slowprint(color_text("\nThat is not a valid percent, try again", "red"), 0.03)
        return tip(cost)
    
    #Convert the raw input to an integer
    try:
        per = int(raw_per)
    except ValueError:
        slowprint(color_text("\nThat is not a valid percent, try again", "red"), 0.03)
        return tip(cost)
    
    #Prevent the user from entering values that are not in the table of tip %'s
    if per not in percent:
        slowprint(color_text("\nThat is not a valid percent, try again", "red"), 0.03)
        return tip(cost)
    
    #If the percent inputted is in the table
    if per in percent:
        #Calculate the $ amount of tip to be added to the total
        tip_amount = cost * percent[per]
        slowprint(f"\n${tip_amount:.2f} added as tip.", 0.03)
    return tip_amount

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