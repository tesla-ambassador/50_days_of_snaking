# You are given a list of names, and you are asked to write a code that returns all the names that start with ‘S’. 
# Your code should return a dictionary of all the names that start with S and how many times they appear in the dictionary. 
# Here is a list below:
# names = ["Joseph","Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera”, "Patel", "Sera"]
# Your code should return: {“Sasha”: 1, “Sera”: 2}

names = ["Joseph", "Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]

def s_names(ls):
    s_dic = {}
    s_counter = 1
    for i in ls:
        if 'S' in i[0]:
            if i in s_dic:
                s_dic[i] = s_counter + 1
            else:
                s_dic[i] = s_counter
    return s_dic

print(s_names(names))