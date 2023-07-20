# Write a function called prime_numbers. This function asks a user to enter a number (integer) as an argument 
# and returns a list of all the prime numbers within its range. 
# For example, if user enters 10, your code should return [2, 3, 5, 7] as prime numbers.

def check_prime(num):
    primes = False
    counter = 0
    for i in range(1, num + 1):
      if num % i == 0:
          counter += 1
    if counter <= 2:
        primes = True
    return primes

def prime_numbers(num):
    prime_array = []
    for i in range(2, num + 1):
       if check_prime(i):
           prime_array.append(i)
    return prime_array

print(prime_numbers(10))