# Write a function called word_index that takes one argument, a list of strings and returns the index of the longest word in the list. 
# If there is no longest word (if all the strings are of the same length), the function should return zero (0). 
# For example, the list below should return 2.

words1 = ["Hate", "remorse", "vengeance"]
words2 = ["Love", "Hate"]

def word_index(ls):
    longest_index = len(ls[0])
    ind = 0
    for i in ls:
        if len(i) > longest_index:
            longest_index = len(i)
            ind = ls.index(i)
    return ind
            
print(word_index(words1))        