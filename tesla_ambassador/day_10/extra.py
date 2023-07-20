# Your new company has a list of figures saved in a list. The issue is that these numbers have no separator. 
# The numbers are saved in the following format:
# [1000000, 2356989, 2354672, 9878098].
# You have been asked to write a code that will convert each of the numbers in the list into a string. 
# Your code should then add a comma on each number as a thousand separator for readability. 
# When you run your code on the above list, your output should be:
# [ '1,000,000', '2,356,989', '2,354,672', '9,878,098’]
# Write a function called convert_numbers that will take one argument, a list of numbers above.

def add_separator(num_ls):
   str_ls = []
   for num in num_ls:
       str_num = str(num)
       pointer = len(str_num)
       counter = pointer - 1
       for i in range (1, pointer + 1):
           if i % 3 == 0:
               str_end = ',' + str_num[counter:]
               str_start = str_num[0:counter]
               str_num = str_start + str_end
           counter -= 1
       str_ls.append(str_num)   
   return str_ls
           
               

print(add_separator([1000000, 2356989, 2354672, 9878098]))