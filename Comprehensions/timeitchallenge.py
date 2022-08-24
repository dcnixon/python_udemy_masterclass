# In the section on Functions, we looked at 2 different ways to calculate the factorial
# of a number.  We used an iterative approach, and also used a recursive function.
#
# This challenge is to use the timeit module to see which performs better.
#
# The two functions appear below.
#
# Hint: change the number of iterations to 1,000 or 10,000.  The default
# of one million will take a long time to run.
 
import timeit
 

def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result
 
 
def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


test_range = range(1, 12)

store_facts = [fact(n) for n in test_range]
print(store_facts)

facts = "[fact(n) for n in test_range]"
factorials = "[factorial(m) for m in test_range]"

number = 100000
result1 = timeit.timeit(facts, number=number, globals=globals())
result2 = timeit.timeit(factorials, number=number, globals=globals())

print("fact function results:     \t{}".format(result1))
print("factorial function results:\t{}".format(result2))
