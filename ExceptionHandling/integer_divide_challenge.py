import sys


def get_input(prompt):
    """Ask for a whole number until 2 valid integers are supplied by the user"""
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Not a whole number")
        except EOFError:
            sys.exit(0)
        finally:
            print("The finally clause always executes")


first_number = get_input("Please enter the first number: ")
second_number = get_input("Please enter the second number: ")

try:
    result = first_number / second_number
    print("{} divided by {} is {}".format(first_number, second_number, result))
except ZeroDivisionError:
    print("Cannot divide by 0.")
    sys.exit(2)
else:
    print("Division performed successfully")

# while True:
#     try:
#         first_number = int(input("Please enter a whole number "))
#         print("Number accepted")
#     except TypeError:
#         "Please enter a valid whole number"
#     try:
#         second_number = int(input("Please enter another whole number "))
#     except:
#         "Please enter a valid whole number"
#
#     try:
#         result = first_number // second_number
#         break
#     except (ZeroDivisionError):
#         print("Cannot divide by zero")
#         continue
#
#
#
#
#
# print("{0} divided by {1} equals {2}".format(first_number, second_number, result))