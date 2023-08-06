# Qns: https://leetcode.com/problems/3sum/

# Rejected - exceeded time limit
class MySolution:
    def threeSum(self, nums):
        sol = []

        for first_idx, first_num in enumerate(nums):
            if first_idx == len(nums) - 2:  # Stop if first number is the second last number in nums list
                break   
            for second_idx, second_num in enumerate(nums[first_idx + 1:], first_idx + 1):
                if second_idx == len(nums) - 1:     # Stop if second number is last number in nums list
                    break
                if (first_num + second_num == 0):       
                    if 0 in nums[second_idx + 1:]:  # Check first num + second num == 0, can still include to sol if third num == 0
                        if sorted([first_num, second_num, 0]) not in sol: 
                            sol.append(sorted([first_num, second_num, 0]))
                    continue
                for third_idx, third_num in enumerate(nums[second_idx + 1:], second_idx + 1):
                    if (first_num + second_num + third_num == 0):
                        if sorted([first_num, second_num, third_num]) not in sol: 
                            sol.append(sorted([first_num, second_num, third_num]))  
        
        return sol


# Sort and binary search
class Solution:
    def threeSum(self, nums):
        nums.sort()
        sol = []
        
        for left in range(len(nums) - 2):   # Stop when reached the last 2 numbers 
            # To avoid duplications from the left side
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            # Taking 2 pointers and using Binary Search
            mid, right = left + 1, len(nums) - 1
            while mid < right:
                curr_sum = nums[left] + nums[mid] + nums[right]
                # Increase the value from the left side
                if curr_sum < 0:
                    mid += 1
                # Decrease the value from the right side
                elif curr_sum > 0:
                    right -= 1
                else:
                    sol.append([nums[left], nums[mid], nums[right]])
                    # Avoid repetition from the sub-array's left side
                    while mid < right and nums[mid] == nums[mid + 1]:
                        mid += 1
                    # Avoid repetition from the sub-array's right side
                    while mid < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    mid += 1
                    right -= 1
        return sol
    

# Driver
nums = [-1,0,1,2,-1,-4]

s = MySolution()
print(s.threeSum(nums))
