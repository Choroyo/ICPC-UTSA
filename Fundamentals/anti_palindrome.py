#Bryan Chora 11/05/2024 Kattis: Anti-Palindrome

'''
'''
#Get words from the user and store in array
line = input()

simpleString = ''.join(char.lower() for char in line if char.isalnum())

inversString = simpleString[::-1]

isPalindrome = False

print(simpleString,inversString)
for i in range(len(simpleString) - 1):
    print( simpleString[i] , inversString[(len(simpleString) - 1) - (i + 1)])
    if simpleString[i] == inversString[(len(simpleString) - 1) - (i + 1)]:
        print( simpleString[i + 1] , inversString[(len(simpleString) - 1) - i])
        if simpleString[i + 1] == inversString[(len(simpleString) - 1) - i] and i < len(simpleString):
            isPalindrome = True
            break
if isPalindrome:
    print("Palindrome")
else:
    print("Anti-palindrome")
    

