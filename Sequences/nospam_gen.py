menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "bacon", "spam", "tomato","spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# Method 1 Remove spam from each list,
# then print the list.

# for meal in menu:
#     top_index = len(meal) - 1
#     for index, item in enumerate(reversed((meal))):
#         if item == "spam":
#             del meal[top_index - index]
#     print(meal)


# Method 2 Print out the items in each list,
# as long as its not spam

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=", ")
    print()
