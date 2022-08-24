available_parts = [("computer", 589),
                   ("monitor", 149),
                   ("keyboard", 59),
                   ("mouse", 33),
                   ("hdmi cable", 48),
                   ("dvd drive", 64),
]
PART_NAME = 0
PART_PRICE = 1

# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = [] # create an empty list
order_total = 0

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part_name = available_parts[index][PART_NAME]
        chosen_part_price = available_parts[index][PART_PRICE]

        if chosen_part_name in computer_parts:
            # it's already in so remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part_name)
            order_total = order_total - chosen_part_price # subtracts the part price to the order total
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part_name) # adds item names to the list
            order_total = order_total + chosen_part_price # ads the part price to the order total
        print("Your list now contains: {} \nCurrent total: ${}"
              .format(", ".join(computer_parts), order_total))
    else:
        print("Please add options from the list below:")
        for number, (part, price) in enumerate(available_parts):
            print("{0}. {1} ${2}".format(number +1, part, price))

    current_choice = input()

print("You have ordered: {} \nTotal: ${}".format(", ".join(computer_parts), order_total))
