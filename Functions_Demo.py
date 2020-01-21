def min_max(numbers):
    '''
    Simple function to find the maximum and minimum numbers in the list of integer values
    '''
    small = large = numbers[0]
    for item in numbers:
        if item > large:
            large = item
        elif item < small:
            small = item
    return small, large


# print(min_max([4, 1, 5, 2, 6, 88, -1, 9]))

# Arguments related to functions
# 1. Default arguments
def func(a, b=12, c=100):
    '''
    You can assign a default value for the arguments in the function declaration.
    This will be overwritten if you pass a different value in the arguments of function calling
    '''
    print('a is :', a, 'b is : ', b, 'c is :', c)


# func(3, b=66)
# print(func.__doc__)             # command to find the doc string

#*******************************************************************************
# 2. Variable length arguments
def total(initial=10,*numbers):
    '''
    Function to calculate the sum of given numbers
    in variable length arguments you can pass multiple numbers in the function calling
    '''
    count=initial
    for num in numbers:
        count+= num
    return count

# print(total(5, 1, 2, 3, 4))
#*****************************************************************************************
# 3. Keyword arguments
def total1(initial=5,*numbers, **keywords):
    '''
    this key word Function is used to calculate the sum of given numbers along with the value count in key
    usinng keyword arguments you can acess the values of keys
    __Keyword arguments should be passed in the last argument__
    '''
    count=initial
    for num in numbers:
        count += num
    for key in keywords:
        count += keywords[key]
    return count
# print(total1(10, 1, 2,3, languages = 20, tools= 50))
#**********************************************************************************
# calculate sum of intergers Using formula based approach
def SumOfIntegers(lb,ub):
    l = lb -1
    return (ub * (ub + 1)) / 2 - ((l * (l - 1)) /2)

# print(SumOfIntegers(1,10))

# Calcukate sum of integers using loop
def sum(lb, ub):
    total = 0
    for i in range(lb, ub + 1):
        total+= i
    return total
# print(sum(1,10))
#********************************************************************************************
# 3. Lambda functions
def sumL(lb, ub, func):
    '''
    argument "func" is nothing but a function
    '''
    total = 0
    for i in range(lb, ub + 1):
        print(func(i))
        total+= func(i)
    return total
# print(sumL(5, 10, lambda i: i))
# print("-----------------")
# print(sumL(5, 10, lambda i: i*i))                           # Printing sum of squares
# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# print(sumL(5, 10, lambda i: i if (i % 2 == 0) else 0))      # printing and adding  even numbers b/w 1 to 10
#******************************************************************************************************************
# Using Map, Filter, Reduce

l = list(range(1,50))
lEven = filter(lambda f: f % 2 == 0, l )
# for i in lEven:
    # print(i)
#
lEven = filter(lambda f: f % 2 == 0, l)             # Filter even numbers from list "l" using lambda function
lsquare = map(lambda f: f * f, lEven)               # Square the even numbers by using map function
import functools as ft
lsum = ft.reduce(lambda x ,y: x + y, lsquare)       # sum of squares of even numbers from 1 to 50
print(lsum)
# help(ft.reduce)