# Problem: https://leetcode.com/problems/plus-one/description/

# My solution
class MySolution:
    def plusOne(self, digits):
        digits = int("".join(map(str, digits)))     # convert to int
        digits += 1     # add 1 
        digits = [int(digit) for digit in str(digits)]     # convert back to list 

        return digits
    

# Driver
digits = [1, 2, 3]

s = MySolution()
print(s.plusOne(digits))
