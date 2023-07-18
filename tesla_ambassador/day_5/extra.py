# You work for a school and your boss wants to know how many female and male students are enrolled in the school. 
# The school has saved the students in a list. 
# Your task is to write a code that will count how many males and females are in the list. 
# Here is a list below:
students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
# Your code should return a list of tuples. The list above should return:
# [(‘Male’,7), (‘female’,6)]

def gender_count(ls):
    male_count = 0
    female_count = 0
    for i in ls:
        if i == 'male' or i == 'Male':
            male_count += 1
        else:
            female_count += 1
    gender_list = [('Male', male_count), ('Female', female_count)]
    return gender_list

print(gender_count(students))
