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

#input skill in range n
for _ in range(n):
    #get input
    keyword = input()
    #normalize the input
    skill = (keyword.replace('-', ' ')).lower()
    #add the skill into the array
    keywords.append(skill)

#print the number of unique skills 
print(len(set(keywords)))    
