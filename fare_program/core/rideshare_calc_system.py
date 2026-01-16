# =============== Imports ===============
import sys
import random

from sfx.text import slowprint, color_text, sep
from fare_program.core.calculation import fare_calc, tip, receipt
from fare_program.map.map import Locations, print_map
from fare_program.user.user import User
from sfx.sfx import loading_bar

# =============== Global Variables ===============
#Flag for while loop
active_drive = False

# =============== Main Program ===============
#Random duration and step count for variability with the loading bar
dur = random.randint(1, 5)
step = random.randint(10, 50)

sep()

try:
    user = User(input("Enter your name:\n > "))
except (KeyboardInterrupt, EOFError):
    slowprint("\nNot sure thats something you can say or do, rude", 0.03)
    sys.exit()

try:
    set_drive = input("\nDo you want to go for a drive? (y/n)\n > ")
except (KeyboardInterrupt, EOFError):
    slowprint("\nNot sure thats something you can say or do, rude", 0.03)
    
if set_drive == "y":
    active_drive = True
elif set_drive == "n":
    slowprint("\nThats fine, have a great day!", 0.03)
else:
    slowprint("\nNot sure thats something you can say or do, rude", 0.03)

world = Locations()

while active_drive:
    print_map()

    slowprint(f"\nYou are currently at {user.location.title()}", 0.03)

    connections = world.map[user.location]["connections"]

    slowprint("\nYou can travel to:", 0.03)
    for place in connections:
        minutes = world.travel_time_minutes(user.location, place)
        slowprint(f" - {place.title()} ({minutes} min)", 0.01)

    try:
        loc = input("\nWhere do you want to go? (Type 'q' to quit)\n > ").lower().strip()
    except (KeyboardInterrupt, EOFError):
        slowprint(color_text("\n- Use an actual location", "red"), 0.03)
        continue

    # Expand abbreviations if provided
    loc = world.abbreviations.get(loc, loc)

    if loc not in connections:
        slowprint(color_text("\n- You can't go there directly from here.", "red"), 0.03)
        continue

    if loc == "q":
        slowprint("\nThanks for driving with us, have a great day!", 0.03)
        break

    minutes = world.travel_time_minutes(user.location, loc)

    # Convert time to distance-based fare (example: 0.5$ per minute)
    km_equivalent = minutes
    fare = fare_calc(km_equivalent)

    slowprint("\nCalculating cost\n", 0.03)
    loading_bar(dur, step)

    slowprint(color_text(f"\nTravel time: {minutes} minutes", "cyan"), 0.03)
    slowprint(color_text(f"Your total is: ${fare:.2f}", "green"), 0.03)

    tip_accept = input("\nWould you like to add a tip? (y/n)\n > ").strip().lower()
    if tip_accept in ["y", "yes"]:
        tip_amount = tip(fare)
    
    elif tip_accept in ["n", "no"]:
        tip_amount = 0.0
        slowprint("\nNo tip added.", 0.03)
    else:
        tip_amount = 0.0
        slowprint("\nInvalid input, no tip added.", 0.03)

    total_cost = fare + tip_amount

    receipt_print = input("\nWould you like a receipt? (y/n)\n > ").strip().lower()
    if receipt_print in ["y", "yes"]:
        receipt(fare, tip_amount, total_cost)

    elif receipt_print in ["n", "no"]:
        slowprint("\nNo receipt printed.", 0.03)

    else:
        slowprint("\nInvalid input, no receipt printed.", 0.03)

    # Update player location
    user.location = loc
