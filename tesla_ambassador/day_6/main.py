# Write a function called user_name that generates a username from the user’s email. 
# The code should ask the user to input an email and the code should return everything before the @ sign as their user name. 
# For example, if someone enters ben@gmail.com, the code should return ben as their user name.

user_input = input('Please input an email to get a user name\nDo not forget the "@": ')
user_list = user_input.split('@')
def user_name(ls):
    return ls[0]
print(user_name(user_list))