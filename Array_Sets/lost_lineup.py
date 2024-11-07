#Bryan Chora 11/07/2024 Kattis: Lost Lineup

"""
This program will try to print the original lineup of n
people depending on the distances from person 1 which is 
Jimmy
"""
#The number of people
numPeople = int(input())

lineUp = [0] * numPeople

lineUp[0] = 1

distances = list(map(int,input().split()))

print(distances)

for i in range(1, numPeople):
    position = 1 + distances[i - 1]
    if 1 <= position < numPeople:  
        lineUp[position] = i + 1

print(*lineUp)