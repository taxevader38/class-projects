from sfx.sfx import loading_bar
from sfx.text import slowprint, color_text, sep

user_quit = False

while not user_quit:
    sep()
    try:
        user_input = input("Select an operation (+, -, *, /) or 'q' to quit: ")
    except (KeyboardInterrupt, EOFError):
        slowprint("\nExiting the calculator. Goodbye!", 0.03)
        break

    if user_input.lower().strip() == 'q':
        slowprint("\nExiting the calculator. Goodbye!", 0.03)
        user_quit = True
        continue

    if user_input not in ['+', '-', '*', '/']:
        slowprint(color_text("\nInvalid operation. Please try again.", "red"), 0.03)
        continue

    if user_input in ['+', '-', '*', '/']:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            slowprint(color_text("\nInvalid number input. Please enter numeric values.", "red"), 0.03)
            continue
        except (KeyboardInterrupt, EOFError):
            slowprint("\nExiting the calculator. Goodbye!", 0.03)
            break

        if user_input == '+':
            result = num1 + num2
        elif user_input == '-':
            result = num1 - num2
        elif user_input == '*':
            result = num1 * num2
        elif user_input == '/':
            if num2 == 0:
                slowprint(color_text("\nError: Division by zero is not allowed.", "red"), 0.03)
                continue
            result = num1 / num2

        loading_bar(2, 20)
        raw_binary_result = bin(int(result))  # Convert result to binary
        bin_result = raw_binary_result[2:]  # Remove '0b' prefix

        slowprint(f"\nThe result of {num1} {user_input} {num2} is: {result}", 0.03)
        slowprint("As a binary value this would be: " + bin_result + "\n", 0.03)