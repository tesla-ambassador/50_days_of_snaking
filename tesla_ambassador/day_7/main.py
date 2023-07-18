# Write a function called string_range that takes a single number and returns a string of its range. 
# The string characters should be separated by dots(.) 
# For example, if you pass 6 as an argument, your function should return ‘0.1.2.3.4.5’.

user_input = int(input('Please enter a single digit: '))

def string_range(num):
    num_array = []
    for i in range(0, num):
        num_array.append(str(i))
    return ('.').join(num_array)

print(string_range(user_input))