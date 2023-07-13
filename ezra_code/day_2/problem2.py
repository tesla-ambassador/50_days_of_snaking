def check_duplicates(list):
    new_set = set()
    duplicates = []
    for x in list:
        if x in new_set:
            duplicates.append(x)
        else:
            new_set.add(x)
    return duplicates


print(check_duplicates(['apple', 'orange', 'banana', 'apple']))
