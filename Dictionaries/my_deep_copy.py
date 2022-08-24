from contents import recipes

def my_deep_copy(d: dict) -> dict:
    """Copy a dictionary, creating copies of the `list` or `dict` values.

    The function will crash with AttributeError if the values aren't
    lists or dictionaries.
    """
    copy = {}
    for key in d:
        copy_value = d[key]
        copy[key] = copy_value.copy()
    return copy


recipes_copy = my_deep_copy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])     # 300
print(recipes["Butter chicken"]["ginger"])          # 3