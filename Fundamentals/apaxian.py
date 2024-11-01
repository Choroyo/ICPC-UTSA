#Bryan Chora 10/31/2024 Kattis: Honour Thy (Apaxian) Parent 
'''
This code will append to string in the following formatings
If Y ends with e, then the extended name is Y + x + P
If Y ends with any other vowel (a,i,o, or u), we remove that final vowel from Y, and then extend Y with ex + p 
If Y already ends with ex, then the extended name is simply Y + P.
Where Y and P are the strings to be appended
'''
y, p = map(str,input().split())

substring = ''

# If y ends with the char e it will append "e" as follow y + x + p
if y[len(y) - 1] == 'e' :
    substring = y + 'x' + p
elif y[len(y) - 1] == 'a' or y[len(y) - 1] == 'i' or y[len(y) - 1] == 'o' or y[len(y) - 1] == 'u':
    substring = y[0 : len(y)-1] + "ex" + p
elif y[len(y) -1] == 'x' and y[len(y) - 2] == 'e':
    substring = y + p
else:
    substring = y + "ex" + p

print (substring)
