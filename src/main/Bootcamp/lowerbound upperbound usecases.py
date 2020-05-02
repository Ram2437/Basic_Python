
def sum(n):
    return int(n * (n + 1) / 2)

def sumOfIntegers(lb, ub):
    return sum(ub) - sum(lb - 1)

# print(sumOfIntegers(5, 10))


def mysum(lb, ub, f):                   # Higher order functions
    total = 0
    for i in range(lb, ub + 1):
        # print(i)
        total += f(i)           # in order to satisfy this function we either user a named function or lambda function
        print(total)
    return total

def i(n): return n                      #Named functions
def sqr(n): return n * n

# print(mysum(5, 10, i))
# print(mysum(5, 10, sqr))

# print(mysum(5, 10, lambda x: x))        # lanbda function
print(mysum(1, 4, lambda x: x ** 2))
# print(mysum(5, 10, lambda x: x ** 3))
# print(mysum(5, 10, lambda x: x if x % 2 == 0 else 0))





