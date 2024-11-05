#Bryan Chora 11/05/2024 Kattis: Triple Texting 

#input string
tripleWord = input()

#The lenght of the string 
wordLen = len(tripleWord) /3

#Initilize array to hold the subtrings of words
words = []

word = ""

#Loop trought the string
for char in tripleWord:
    # If the size of the substring still lower than the size word
    if len(word) < wordLen:
        #Add a character to the word
        word += char
    #if is the same size append the word to the array of words and empty the word
    if len(word) == wordLen:
        words.append(word)
        word = ""

#Loop trought the elements inside the array 
for string in words:
    #If the word is repeated 2 times is the correct or more
    count = words.count(string)
    if count > 1:
        #Print the correct word
        print(string)
        break