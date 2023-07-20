# Write a function called odd_even that has one parameter and takes a list of numbers as an argument. 
# The function returns the difference between the largest even number in the list and the smallest odd number in the list. 
# For example, if you pass [1,2,4,6] as an argument the function should return 6 -1= 5.

user_input = input('Please input an array of integers separated by comma (", ")\nDo not forget the space after the comma: ')
user_list = user_input.split(', ')
user_number_list = []
for i in user_list:
    user_number_list.append(int(i))

def odd_even(ls):
    largest_even = 0
    smallest_odd = []
    for i in ls:
        if i % 2 == 0:
            if i > largest_even:
                largest_even = i
        else:
            smallest_odd.append(i)
    return largest_even - min(smallest_odd)

print(odd_even(user_number_list))