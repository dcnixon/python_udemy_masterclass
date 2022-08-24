from contents import pantry, recipes


def add_to_shopping_list(data: dict, item: str, amount: int) -> None:
    """Add a dict containing `item` and `amount` to the `data` dict"""
    # try:
    #     data[item] += amount
    # except KeyError:
    #     data[item] = amount
    data[item] = data.setdefault(item, 0) + amount
    return None


display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}

shopping_list = {}
# display the recipes we know how to cook
while True:
    print("Please choose a recipe")
    print("-" * 20)
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input("> ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            pantry_quantity = pantry.get(food_item, 0)
            if required_quantity <= pantry_quantity:
                print(f"\t{food_item} OK")
            else:
                buy_quantity = required_quantity - pantry_quantity
                print(f"\tYou need to buy of {buy_quantity} of {food_item}.")
                add_to_shopping_list(shopping_list, food_item, buy_quantity)
for things in shopping_list.items():
    print(things)
        # if all(ingredients) in pantry:
