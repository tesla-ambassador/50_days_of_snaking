# Write a function called Python_snakes that takes a number as an argument 
# and creates the following shape, using the number’s range: (hint: Use the loops and emoji library. 
# If you pass 7 as argument, your code should print the following:

user_input = int(input('Please input a number: '))

def python_snakes(num):
    for i in range(1, num + 1):
        for j in range(1, i):
            print('#', end=' ')
        print()

python_snakes(user_input)