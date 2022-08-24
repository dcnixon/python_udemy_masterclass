# numbers = input("Please enter 3 numbers separated by commas: ")
# a, b, c = numbers.split(',')
# result = int(a) + int(b) - int(c)
# print(result)


def sum_eo(n:int, t:str):
    if t == 'e':
        return sum(range(0, n, 2))
    elif t == 'o':
        return sum(range(1, n, 2))
    else:
        return -1


print(sum_eo(10, 'e'))
print(sum_eo(7, 'o'))
print(sum_eo(11, 'spam'))
