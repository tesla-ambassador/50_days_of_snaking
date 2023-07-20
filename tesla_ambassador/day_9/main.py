# Create a function called biggest_odd that takes a string of numbers and returns the biggest odd number in the list.
# For example, if you pass ‘23569’ as an argument, your function should return 9. Use list comprehension.

user_input = input('Please input a long number... Not necessarily long though (Also no decimal places): ')
# Separating the numbers into separate strings.
def biggest_odd(st):
    user_list = []
    largest_odd = 0
    for i in st:
        user_list.append(int(i))
    for j in user_list:
        if j % 2 != 0:
            if j > largest_odd:
                largest_odd = j
    return largest_odd

print(biggest_odd(user_input))