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


# Driver
nums = [0,1,1]

s = MySolution()
print(s.threeSum(nums))
