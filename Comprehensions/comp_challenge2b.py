import timeit

setup = """\
gc.enable()
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}
 
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}
"""

print("nested for loops")
print("================")
nested_loop = """\
for location in locations:
    exits_to_destination_1 = []
    for key in exits:
        if location in exits[key].values():
            exits_to_destination_1.append((key, locations[key]))
    print("locations leading to: {}".format(location), end="\t")
    print(exits_to_destination_1)
"""
print()

print("list comprehension inside a for loop")
print("====================================")
loop_comp = """\
for location in locations.keys():
    exits_to_destination_2 = [(key, locations[key]) for key in exits if location in exits[key].values()]
    print("locations leading to: {}".format(location), end="\t")
    print(exits_to_destination_2)
"""
print()

print("nested comprehension")
print("====================")
nested_comp = """\
exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
                          for loc in locations]
for index, loc in enumerate(exits_to_destination_3):
    print("locations leading to: {}".format(index), end="\t")
    print(loc)
"""

result_1 = timeit.timeit(nested_loop, setup, number=10000)
result_2 = timeit.timeit(loop_comp, setup, number=10000)
result_3 = timeit.timeit(nested_comp, setup, number=10000)

print("Nested loop:\t{} seconds".format(result_1))
print("Loop comp:  \t{} seconds".format(result_2))
print("Nested comp:\t{} seconds".format(result_3))