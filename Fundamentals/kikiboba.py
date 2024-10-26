#Bryan Chora 09/15/2024 Kattis: Kiki Boba
'''
If there is not (B) or (K) this will print none
if there is more (B) than (K) will print "boba"
if there is more (K) than (B) will print "kiki"
if there is a equal number of count is gonna be "boki"
'''

word = input()

countB = 0

countK = 0

for char in word:
    if char == 'b':
        countB = countB + 1
    if char == 'k':
        countK = countK + 1

if countB == 0 and countK == 0:
    print("none")
elif countB > countK:
    print("boba")
elif countB < countK:
    print("kiki")
elif countB == countK:
    print("boki")