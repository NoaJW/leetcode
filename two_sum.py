# Problem: https://leetcode.com/problems/two-sum/?envType=featured-list&envId=top-interview-questions 

# My solution
class MySolution:
    def twoSum(self, nums, target):
        for counter, item in enumerate(nums):
            complement = target - item
            if complement in nums: 
                if counter != nums.index(complement):   # It is ok to check against the first occurence of the complement, since the qns requires only 1 ans and not multiple possibilities. 
                    return [counter, nums.index(complement)]


# Optimized solution
class Solution:
    def twoSum(self, nums, target):
        num_to_index = {}

        for counter, item in enumerate(nums):
            if target - item in num_to_index:   
                return [num_to_index[target - item], counter]

            num_to_index[item] = counter    # Set the key as item, value as counter
        
        return []   # Return an empty list if there is no ans
    

# Driver
nums = [2,7,11,15]
target = 9

s = MySolution()
print(s.twoSum(nums, target))




