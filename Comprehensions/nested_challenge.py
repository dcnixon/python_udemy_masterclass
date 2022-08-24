# use a nested comprehension to produce the times tables for values from 1 to 10

for i in range(1, 11):
    for j in range (1, 11):
        print(i, i * j)
print("=" * 40)

times = [print(i, i * j) for i in range(1, 11) for j in range(1, 11)]
print(times)

for x, y in [print(i, i * j) for i in range(1, 11) for j in range(1, 11)]:
    print(x, y)
