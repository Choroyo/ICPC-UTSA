#Bryan Chora 11/07/2024 Kattis: Forced Choice

"""
This program will check for a set of cards to keep the last
card the one to be chosen(secret) by making sure to remove
every card that is not in the same set chosen 
"""
cards, secret, steps = map(int,input().split())

setCards = set(range(1, cards + 1))

for _ in range(steps):
    numbers = list(map(int,input().split()))
    setChosen = set(numbers[1:])
    if secret in setChosen:
        print("KEEP")
        setCards = setChosen
    else:
        print("REMOVE")
        setCards -= setChosen