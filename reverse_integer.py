# Problem: https://leetcode.com/problems/reverse-integer/

class MySolution:
    def reverse(self, x):
        string_num = str(x)
        new_string_num = ""

        if x >= 0:
            for i in string_num[-1::-1]:
                new_string_num += i
        else:
            new_string_num += "-"
            for i in string_num[-1:0:-1]:
                new_string_num += i

        new_string_num.strip("0")

        new_num = int(new_string_num)

        if new_num >= -(2 ** 31) and new_num < 2 ** 31:
            return new_num
        else:
            return 0


class Solution:
    def reverse(self, x):
        reversed_num = int(str(abs(x))[::-1]) * (-2 * (x < 0) + 1)  # slice in reverse order positive x, convert it to an int and multiply it with 1 or -1 if it is negative
        return reversed_num if -2 ** 31 <= reversed_num < 2 ** 31 else 0    # return the reversed number if it is within the 32-bit signed integer's range, else return 0 


# Driver
x = 123

s = MySolution()
print(s.reverse(x))