# Problem: https://leetcode.com/problems/single-number/

from collections import Counter
from functools import reduce

class MySolution:
    def singleNumber(self, nums):
        c = Counter(nums)
        print(c.most_common()[-1][0])


class Solution1: 
    def singleNumber(self, nums):
        dict = {}

        for i in nums: 
            if i not in dict.keys():
                dict[i] = 1
            else:
                dict[i] += 1

        for key, val in dict.items():
            if val == 1:
                print(key) 


# With XOR, but it seems to work only in this special case where all numbers have dupes and one is by itself
class Solution2: 
    def singleNumber(self, nums):
        return reduce(lambda x, y: x ^ y, nums)


# Driver
nums = [2, 2, 1]

s = MySolution() 
print(s.singleNumber(nums))

