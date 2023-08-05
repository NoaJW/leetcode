# Problem: https://leetcode.com/problems/happy-number/

class MySolution:
    def isHappy(self, n):
        dict = {}
        sum = 0

        # Stop looping when n is already in dict 
        # Qns: Not sure why adding an int as key will automatically turn into a string 
        while (not str(n) in dict): 
            n = str(n)

            for i in n:
                sum += int(i)**2

            dict[n] = sum
            n = sum 
            sum = 0
    
        return ("1" in dict)


class Solution:
    def isHappy(self, n):
        dict = {}

        while not n in dict:
            l = [int(i)**2 for i in str(n)]
            squared_sum = sum(l)
            dict[n] = squared_sum
            n = squared_sum
            
        return 1 in dict


# Driver
n = 19

s = MySolution()
print(s.isHappy(n))