#Bryan Chora 11/07/2024 Kattis: Forced Choice

"""
This program will keep the set of cards where the secret card belongs then every time is
gonna try to remove the card that we dont need withour removing the card that is secret
and the end of all command the secret card is gonna only remains in the set card
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