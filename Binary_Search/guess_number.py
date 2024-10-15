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