panagram = """The quick brown
fox jumps\tover
 he lazy dog"""

words = panagram.split()
print(words)


values = "9,223,372,036,854,775,807"
values_list = (values.split(","))


print(values)
print(values_list)

# make a new list with ints
integer_values = []
for value in values_list:
    integer_values.append(int(value))

print(values_list)
print(integer_values)


# Use a for loop to produce a list of ints rather than strings.
# You can either modify the contents of the 'values_list' list in place,
# or create a new list of ints.

# replace the values in place
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])

print(values_list)