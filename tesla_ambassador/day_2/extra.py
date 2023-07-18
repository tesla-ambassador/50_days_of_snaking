# Write a function called check_duplicates that takes a list of strings as an argument. 
# The function should check if the list has any duplicates. 
# If there are duplicates, the function should return the duplicates. 
# If there are no duplicates, the function should return "No duplicates". 
# For example, the list of fruits below should return apple as a duplicate and list of names should return "no duplicates".
# fruits = ['apple', 'orange', 'banana', 'apple'] names = ['Yoda', 'Moses', 'Joshua', 'Mark']

fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']
user_input = input("Please input a list of strings separated by a comma\nDon't forget the space after the comma: ")
user_list = user_input.split(', ')

def check_duplicates(ls):
    dup_list = []
    counter = 1
    dup_value = ''
    for i in ls:
        if i in dup_list:
            counter += 1
            dup_value = i
        dup_list.append(i)
    if counter > 1:
        return dup_value
    else:
        return "No duplicates"
print(check_duplicates(user_list))