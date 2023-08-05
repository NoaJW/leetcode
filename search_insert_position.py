# Problem: https://leetcode.com/problems/search-insert-position/

class MySolution:
    def searchInsert(self, nums, target):
        if target not in nums:
            nums.append(target)
            nums.sort()

        return nums.index(target)


class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):      # iterate through the list
            if nums[i] >= target:       # if an item is greater than or equals to the target, return its index
                return i

        return len(nums)                # if all items are smaller than the target, return the additional last index which corresponds to the length of the list 


# Driver
nums = [1,3,5,6]
target = 5

s = MySolution()
print(s.searchInsert(nums, target))