l = 'Python world        '
# help(str.rjust)
# print(ljust(2))

# for i in range(1,10 +1):
#     print(i)

#user defined functions

def sumOf2Nums(lb,ub):
    total = 0
    for i in range(lb, ub + 1):
        total += i
    return print(total)

# sumOf2Nums(1,10)


def sumOfsquares(lb,ub):
    squaresTot = 0
    for i in range(lb, ub + 1):
        squaresTot += i ** 2
    return squaresTot
sumOfsquares(1,10)

# Lambda Functions:

def sumofnums(lb, ub, f):
    sum = 0
    for i in range(lb,ub+1):
        print (i)
        sum += f(i)           # Invoking the function by pasing i as argument,for each iteration "i" we are invoking the function
    return print(sum)

def multilplyBy2(i):           # Named Functions
    return i * 2

def checkEven(i):              # Named Funnctions
    return i if( i % 2  == 0) else 0


print(sumofnums(1, 3, lambda i: multilplyBy2(i)))
print(sumofnums(5, 10, lambda i: multilplyBy2(i)))

# sumofnums(1, 3, lambda s: s)
# sumofnums(1, 3, lambda s: s * s)
# sumofnums(1, 3, lambda s: s ** s)