#Bryan Chora 11/05/2024 Kattis: Anti-Palindrome

'''
'''
#Get words from the user and store in array
line = input()

simpleString = ''.join(char.lower() for char in line if char.isalnum())

isPalindrome = False

if simpleString == simpleString [::-1]:
        isPalindrome = True
else:
    for lenght in range(2, len(simpleString) + 1):
        print(lenght)
        if isPalindrome:
            break
        for i in range(len(simpleString) - lenght + 1):       
            substring = simpleString[i : i + lenght]
            if substring == substring [::-1]:
                isPalindrome = True
        
if isPalindrome:
    print("Palindrome")
else:
    print("Anti-palindrome")


    