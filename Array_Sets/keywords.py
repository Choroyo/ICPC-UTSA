#Bryan Chora 11/07/2024 Kattis: Keywords

"""
This program will normalize the input by changing all the uppercases
to lowercases and by changing the hyphen to spaces and will
store the data into in a array and converted in a set to check 
the different skills inside the set
"""

#The number of skill to input
n = int(input())

#initilize array of keywords
keywords = []

for _ in range(n):
    keyword = input()
    skill = (keyword.replace('-', ' ')).lower()

    keywords.append(skill)

print(len(set(keywords)))    
