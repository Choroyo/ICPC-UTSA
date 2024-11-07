#Bryan Chora 11/07/2024 Leetcode: Custom Sort String
"""
This program will sort the character in where there is two parameter
order and s order is the character that we have to mach first 
with s and create a substring following that order and printed
"""

class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        #Initilize variables
        outOrder = [] # to save the remainder character out of order 
        inOrder = [] # save the character that are in order
        result = "" # to hold the result string after order

        #populate outOrder 
        for char in s:
            outOrder.append(char)
        
        #start sorting by order 
        for ch in order:
            for letter in outOrder[:]:
                #add the character in order and remove from out order
                if ch == letter:
                    inOrder.append(ch)
                    outOrder.remove(letter)

     
        #finish adding char out of order
        for cha in outOrder:
            inOrder.append(cha)
        #add all the char in order into a result string 
        for c in inOrder:
            result += c
        #print result
        return result
"""
solution = Solution()

result = solution.customSortString("kqep","pekeq")

print(result)
"""