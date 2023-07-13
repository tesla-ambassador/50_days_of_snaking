def convert_add(list_of_strings):
    #takes list of strings
    num = 0
    for x in list_of_strings:
        num = num + int(x)
    return num

print(convert_add(['1', '3', '5']))