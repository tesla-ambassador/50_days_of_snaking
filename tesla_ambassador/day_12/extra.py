# Write a function called age_in_minutes that tells a user how old they are in minutes. 
# Your code should ask the user to enter their year of birth, and it should return their age in minutes 
# (by subtracting their year of birth to the current year). Here are things to look out for:
# a. The user can only input a 4-digit year of birth. For example, 1930 is a valid year. 
# However, entering any number longer or less than 4 digits long should render input invalid. 
# Notify the user to input a four digits number.
# b. If a user enters a year before 1900, your code should tell the user that input is invalid. 
# If the user enters the year after the current year, the code should tell the user, to input a valid year.
# The code should run until the user inputs a valid year. 
# Your function should return the user's age in minutes. For example, if someone enters 1930, as their year of birth your 
# function should return:
# You are 48,355,200 minutes old.

from datetime import datetime
current_year = datetime.today().year
print(current_year)
false_input = True
while false_input:
    user_input = input('Enter your date of birth: ')
    if len(user_input) > 4:
        print('Please input a 4 digits number')
    elif int(user_input) < 1900 or int(user_input) > current_year:
        print('Please enter a valid year')
    else:
        false_input = False

def age_in_minutes(num):
    age = current_year - num
    minute_age = age * 525600
    return (f'You are {commas_in_number(minute_age)} minutes old')

def commas_in_number(num2):
    str_num = str(num2)
    pointer = len(str_num)
    counter = pointer - 1
    for i in range(1, pointer + 1):
        if i % 3 == 0:
            str_end = ','+str_num[counter:]
            str_start = str_num[0:counter]
            str_num = str_start + str_end
        counter -= 1
    return str_num

print(age_in_minutes(int(user_input)))
        

