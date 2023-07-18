# Challenge
# Write a function called convert_add that takes a list of strings as an argument 
# and converts it to integers and sums the list. 
# For example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and summed to 9.

user_input = input('Please input a list of numbers separated with commas\n(Do not forget the space after the comma!): ')
example_list = user_input.split(', ')
 
def convert_add(ls):
    final_list = []
    for i in ls:
        final_list.append(int(i))
    return sum(final_list)

print(convert_add(example_list))