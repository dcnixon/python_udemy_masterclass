fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small sweet fruit growing in bunches",
         "lime": "a sour, green citrust fruit",
}

print(fruit)

# # ordered_keys = list(fruit.keys())
# ordered_keys = sorted(list(fruit.keys()))
# # print(ordered_keys)
# # ordered_keys.sort()
# print(ordered_keys)
# for f in ordered_keys:
#     print("{} - {}".format(f, fruit[f]))
#
# print()
# for f in sorted(fruit.keys()):
#     print("{} - {}".format(f, fruit[f]))
# print()
# print(fruit.keys())
#
# for val in fruit.values():
#     print(val)

# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomato"] = "not nice with ice cream"
# print(fruit_keys)
print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print("{} is {}".format(item, description))

print(dict(f_tuple))