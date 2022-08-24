data = [ 4, 5, 104, 105, 110, 120, 130, 130, 150,
         160, 170, 183, 185, 187, 188, 191, 350, 360]
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#          160, 170, 183, 185, 187, 188, 191]
# data = [104, 105, 110, 120, 130, 130, 150,
#          160, 170, 183, 185, 187, 188, 191, 350, 360]
# data = [104, 105, 110, 120, 130, 130, 150,
#          160, 170, 183, 185, 187, 188, 191]
# data = [1104, 1105, 1110, 1120, 1130, 1130, 1150,
#         1160, 1170, 1183, 1185, 1187, 1188, 1191]
# data = []
# data = [104, 101, 4, 105, 308, 103, 5,
#         107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

# for index in range(len(data) - 1, - 1, - 1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)
#         del data[index]

# works better with longer lists - more obvious we are reversing the index
top_index = len(data) - 1
for index, value in enumerate(reversed((data))):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]
print(data)
