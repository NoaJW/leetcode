# Problem: https://leetcode.com/problems/single-number/

class MySolution:
    def __init__(self):
        self.dict = {}

    def singleNumber(self, nums):
        for i in nums:
            # Check if num is in dict
            if self.dict.get(i) != None:
                self.dict[i] += 1
            else:
                self.dict[i] = 1

        for key, val in self.dict.items():
            if val == 1:
                return key  


# Driver
nums = [2, 2, 1, 2, 3]

s = MySolution()
print(s.singleNumber(nums))