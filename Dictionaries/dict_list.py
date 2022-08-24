available_parts = {'1': 'computer',
                   '2': 'monitor',
                   '3': 'keyboard',
                   '4': 'mouse',
                   '5': 'hdmi cable',
                   '6': 'dvd drive',
}
computer_parts = []
current_choice = None
while current_choice != '0':
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]

        if chosen_part not in computer_parts:
            computer_parts.append(chosen_part)
            print(f"Adding {chosen_part}")
        else:
            computer_parts.remove(chosen_part)
            print(f"Removing {chosen_part}")
        print(f"Your list now contains: {computer_parts}")
    else:
        print("Please choose from one of the following options:")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("O: to finish")
    current_choice = input("> ")

print(f"You bought: {', '.join(computer_parts)}")

