#challange 1
#function that takes an argument and returns the square root of the number if divisible by 5

import math

def divide_or_sqaure(x):
    if x % 5 == 0:
        return round(math.sqrt(x),2)
    else:
        return x % 5

print(divide_or_sqaure(10))