choice = "-"
# Respond to a valid input numbered
while choice != "0":
    if choice in "123456":
        print("You chose {}".format(choice))
    else:
        # Print a menu of numbered options
        print("Please choose one dinner option from the list below:")
        print("1.\tbeef")
        print("2.\tchicken")
        print("3.\tham")
        print("4.\tbeans")
        print("5.\trice")
        print("6.\tpotatoes")
        print("0.\tQuit")
    choice = input()