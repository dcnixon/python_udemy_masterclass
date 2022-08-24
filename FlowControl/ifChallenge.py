name = input("Please enter your name: ")
age = int(input("Hello {0}, how old are you? ".format(name)))

if 18 <= age <= 30:
    print("Welcome to the holiday!")
else:
    print("You do not qualify for this holiday")