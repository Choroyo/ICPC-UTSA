#Bryan Chora 10/25/2024 Leetcode: First Bad Version
'''
This will return the first bad version inside a array
where before the first bad version all are good version
and after all are bad version 
'''

class Solution(object):
    def firstBadVersion(self, n):

        low = 1
        high = n

        while low < high:
            mid =(low + high) // 2
            
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

            if isBadVersion(high - 1) == False:
                return(high)

        if isBadVersion(low):
            return(low)
        
        """
        :type n: int
        :rtype: int
        """
        