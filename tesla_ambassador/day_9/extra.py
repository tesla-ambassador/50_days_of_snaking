# Write a function called zeros_last. This function takes a list as argument. 
# If a list has zeros (0), it will move them to the front of the list and maintain the order of the other numbers in the list. 
# If there are no Zeros in the list, the function should return the original list sorted in ascending order. 
# For example, if you pass [1, 4, 6, 0, 7,0,9] as an argument, your code should return [1, 4, 6, 7, 9, 0, 0]. 
# If you pass [2, 1, 4, 7, 6] as your argument, your code should return [1, 2, 4, 6, 7].

def zeros_last1(ls):
    zero_array = []
    if 0 in ls:
        for i in ls:
            if i != 0:
                zero_array.append(i)
        for j in ls:
            if j == 0:
                zero_array.append(j)
        return zero_array
    else:
        ls.sort()
        return ls
    
def zeros_last2(ls):
    zero_array = []
    zero_counter = 0
    if 0 in ls:
        for i in ls:
            if i != 0:
                zero_array.append(i)
            else:
                zero_counter += 1
        while zero_counter > 0:
            zero_array.append(0)
            zero_counter -= 1
        return zero_array
    else:
        ls.sort()
        return ls

print(zeros_last1([1, 4, 6, 0, 7,0,9]))
print(zeros_last1([2, 1, 4, 7, 6]))

print(zeros_last2([1, 4, 6, 0, 7,0,9]))
print(zeros_last2([2, 1, 4, 7, 6]))