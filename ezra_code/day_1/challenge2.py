#Return longest value from dictionary
def longest_value(x):
    long_value = ''
    for value in x.values():
        if (len(value) > len(long_value)) and (len(value) != len(long_value)):
            long_value = value
    return long_value

fruits = {
    'fruit':'apple',
    'color':'green',
}

print(longest_value(fruits))