# Write a function called swap_values. This function takes a list of numbers and swaps the first element with the last element. 
# For example, if you pass [2, 4,67, 7] as a parameter, your function should return
# [7, 4, 67, 2].

def swap_values(ls):
    temp = ls[0]
    ls[0] = ls[len(ls) - 1]
    ls[len(ls) - 1] = temp
    return ls

print(swap_values([2, 4,67, 7]))