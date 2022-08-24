# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import pytz
import random
import datetime

menu_list = [(0, "Quit")]

# Creates a random list of available timezones to choose from
for number, option in enumerate(range(9), 1):
    random_tz = pytz.all_timezones[random.randint(1, len(pytz.all_timezones))]
    menu_list.append((number, random_tz))

# Convert the generated random list to a dictionary with integer keys
menu_options = dict(menu_list)

print("Please select a timezone from the following options to view the time")
for option in sorted(menu_options):
    print("{0}. {1}".format(option, menu_options[option]))

while True:

    choice = int(input("Enter a timezone: "))

    if choice == 0:
        break

    if choice in menu_options.keys():

        selected_tz = pytz.timezone(menu_options[choice])

        selected_tz_time = datetime.datetime.now(tz=selected_tz)

        print("The local time for {0} is: {1} | {2}"
              .format(selected_tz, selected_tz_time.strftime("%A %x %X %z"), selected_tz_time.tzname()))
        print("You local time is: {}".format(datetime.datetime.now().strftime("%A %x %X %z")))
        print("UTC time is: {}".format(datetime.datetime.utcnow().strftime("%A %x %X %z")))


# for option in enumerate(range(9),1):
#     menu_options = random.randint(1,593)
#
# print(len(pytz.all_timezones))
