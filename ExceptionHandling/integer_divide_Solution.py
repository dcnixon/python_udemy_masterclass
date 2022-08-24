import sys


def get_int(prompt):
    """Ask for a whole number until 2 valid integers are supplied by the user"""
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Not a whole number")
        except EOFError:
            sys.exit(1)
        finally:
            print("The finally clause always executes")


first_number = get_int("Please enter the first number: ")
second_number = get_int("Please enter the second number: ")

try:
    result = first_number / second_number
    print("{} divided by {} is {}".format(first_number, second_number, result))
except ZeroDivisionError:
    print("Cannot divide by 0.")
    sys.exit(2)
else:
    print("Division performed successfully")