def factorial(n: int) -> int:
    """Return n!, 0! equals 1"""
    answer = 1
    for value in range(1, n + 1):
        answer *= value
    return answer


for number in range(36):
    print(number, factorial(number))