# Write a function called register_check that checks how many students are in school.
# Your function should return the number of students in school.  
# The function takes a dictionary as a parameter. 
# If the student is in school, the dictionary says ‘yes’. If the student is not in school, the dictionary says ‘no’.
# Use the dictionary below. Your function should return 3. 

register = {'Michael':'yes','John': 'no', 'Peter':'yes', 'Mary': 'yes'}

# Method 1 - Creating a new dictionary in the function
def register_check(dic):
    new_dic = {}
    for key in dic:
        if dic[key] == 'yes':
            new_dic[key] = dic[key]
    return len(new_dic)

# Method 2 - creating a counter variable
def register_check2(dic):
    counter = 0
    for key in dic:
        if dic[key] == 'yes':
            counter += 1
    return counter

print(register_check(register))
print(register_check2(register))