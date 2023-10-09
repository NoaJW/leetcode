# Problem: https://leetcode.com/problems/remove-element/

class MySolution:
    def removeElement(self, nums, val):
        while nums.count(val) > 0:
            nums.remove(val)

        return len(nums)


# Author did not modify array but monitored the length of the list only 
class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0

        start = 0
        end = len(nums) - 1

        while start <= end:
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]         
                end -= 1
            else:
                start += 1
        
        return start
    

# Driver
nums = [3,2,2,3]
val = 3

s = MySolution()
print(s.removeElement(nums, val))