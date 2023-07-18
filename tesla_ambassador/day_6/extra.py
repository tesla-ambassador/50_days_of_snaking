# Write a function called zeroed code that takes a list of numbers as an argument. 
# The code should zero (0) the first and the last number in the list. 
# For example, if the input is [2, 5, 7, 8, 9], your code should return [0, 5, 7, 8, 0].

user_input = input('Please enter a list of numerical values separated by a comma and space ", ": ')
user_list = user_input.split(', ')
num_list = []
for i in user_list:
    num_list.append(int(i))   

def zeroed(ls):
    ls[0] = 0
    ls[-1] = 0
    return ls

print(zeroed(num_list))