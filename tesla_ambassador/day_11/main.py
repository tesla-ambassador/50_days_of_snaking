# Write a function called equal_strings. The function takes two strings as arguments and compares them. 
# If the strings are equal (if they have the same characters and have equal length), it should return True, 
# if they are not, it should return False. For example, ‘love’ and ‘evol’ should return True.

str_1 = 'love'
str_2 = 'evol'

def equal_strings(str_a, str_b):
    for i in str_a:
        if i in str_b and len(str_a) == len(str_b):
            return True
        else:
            return False

print(equal_strings(str_1, str_2))