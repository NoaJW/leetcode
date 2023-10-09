# Problem: https://leetcode.com/problems/jump-game/description/

# My solution - incorrect don't understand qns
class MySolution:
    def canJump(self, nums):
        last_index = len(nums) - 1
        index = 0 

        if index == last_index:     # Check for [0]
            return True

        while index < last_index:
            index += nums[index]

            if index == last_index: 
                return True
            if index > last_index:  # index has exceeded last_index
                return False
            if nums[index] == 0:    # index cannot jump if element is 0
                return False 


# Driver
steps = [2, 0]

s = MySolution()
print(s.canJump(steps))
