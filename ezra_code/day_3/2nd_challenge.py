def lowercaser(list):
    new_list = []
    for _ in list:
        if _.islower():
            new_list.append(_)
    new_list.sort(reverse=True)
    return (new_list)

names = ["kerry", "dickson", "John", "Mary","carol", "Rose", "adam"]

print(lowercaser(names))
