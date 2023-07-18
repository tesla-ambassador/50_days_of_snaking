names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
# You are given a list of names above. This list is made up of names of lowercase and uppercase letters.
# Your task is to write a code that will return a tuple of all the names in the list that have only lowercase letters. 
# Your tuple should have names sorted alphabetically in descending order. Using the list above, your code should return:
# ('kerry', 'dickson', 'carol', 'adam')

def lowercase_tuple_generator(ls):
    lowercase_list = []
    for i in ls:
        if i.islower():
            lowercase_list.append(i)
    return tuple(lowercase_list)

print(lowercase_tuple_generator(names))