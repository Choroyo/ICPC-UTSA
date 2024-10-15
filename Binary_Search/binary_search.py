
target = 9

nums = [-1,0,3,5,9,12]

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
            low = mid - 1
            
        if high == target:
            print(high)
            break
        