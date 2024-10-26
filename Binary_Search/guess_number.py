#Bryan Chora 10/15/2024 Leetcode: Guess Number Higher or Lower 

'''
This I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns three possible results:
-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick)
'''
class Solution(object):
    def guessNumber(self, n):
        low = 1
        high = n

        while True:
            choice = (low + high) // 2

            result = guess(choice)

            if result == 0:
                return choice
            elif result == 1:
                low = choice + 1
            elif result == -1:
                high = choice - 1