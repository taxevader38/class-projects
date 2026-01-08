# =============== Imports ===============
import time

def pause(sec=0.6):
    time.sleep(sec)

def sep():
    print("\n" + "-" * 60 + "\n")

def slowprint(text, delay=0.01):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def color_text(text, color="end"):
    colors = {
        "bold": "\033[1m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "italic": "\033[3m",
        "end": "\033[0m"
    }
    return f"{colors.get(color, '')}{text}{colors['end']}"

def print_clear():
    print("\033c", end="", flush=True)
