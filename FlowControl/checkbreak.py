# Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11

# for i in range(0, 100, 7):
#     print(i)
#     if i < 0 or i % 11 == 0:
#         break
# print numbers to 20 not divisible by 3 or 5

for i in range(0,20):
    if i % 5 == 0:
        continue
    if i % 3 == 0:
        continue
    print(i)