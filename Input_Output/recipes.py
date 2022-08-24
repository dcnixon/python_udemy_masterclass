import shelve

# blt = ["bacon", "lettuce", "tomate", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open('recipes', writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans_on_toast"] = beans_on_toast
    # recipes["scrambled_eggs"] = scrambled_eggs
    # recipes["soup"] = soup
    # recipes["pasta"] = pasta

    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")

    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list


    recipes["soup"] = soup

    recipes["soup"].append("croutons")
    soup.append("cream")

    # The case below is looking directly at the shelve file so we don't
    # see the changes made above
    for snack in recipes:
        print(snack, recipes[snack])
