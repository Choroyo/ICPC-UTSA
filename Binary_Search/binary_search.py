#Bryan Chora 09/15/2024 Leetcode: Binary Search
#This algorithms will do a banary search to fine the target number
#from a sorted array  otherwise will return -1 
class Solution(object):
    def search(self, nums, target):

        def check(n):
            return n >= target
        
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            val = nums[mid]

            if check(val):
                high = mid
            else:
                low = mid + 1
            
        return low if nums[low] == target else -1

        