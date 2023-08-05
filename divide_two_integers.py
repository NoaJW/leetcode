# Problem: https://leetcode.com/problems/divide-two-integers/

# Rejected: time limit exceeded. Since I counted the number of additions to the dividend as the quotient, it is very slow if the divident is large and the divisor is small. 
class MySolution:
    def divide(self, dividend, divisor):
        # If dividend and divisor are both negative 
        if dividend < 0 and divisor < 0: 
            dividend = abs(dividend)
            divisor = abs(divisor)
            return self.general_division(dividend, divisor)
            
        # If dividend and divisor are both positive
        elif dividend >= 0 and divisor >= 0:
            return self.general_division(dividend, divisor)

        # If either the dividend or the divisor is negative
        elif dividend < 0 or divisor < 0: 
            dividend = abs(dividend)                # Take the absolute value of both instead of doing it separately to reduce the number of steps
            divisor = abs(divisor)
            return -self.general_division(dividend, divisor)

    def general_division(self, dividend, divisor):
        if dividend == divisor:
            quotient = 1
        elif dividend < divisor:
            quotient = 0
        else:
            quotient = 0
            sum = 0
            sum_next = 0

            while sum_next < dividend:             
                sum += divisor
                quotient += 1
                sum_next = sum + divisor

        if quotient > 2**31 - 1 or quotient < -2**31:
            return  2**31 - 1
        
        return quotient 


# Bit shifting! 
class Solution(object):
    def divide(self, dividend, divisor):
        flag1 = 1        
        flag2 = 1

        if dividend < 0:            
            flag1 = 0            
            dividend = -dividend        
        if divisor < 0:
            flag2 = 0
            divisor = -divisor
            
        ans = 0
        now = divisor
        bit = 1
        while(dividend > 0):
            if now<<1 > dividend:
                if dividend < divisor:
                    break
                dividend -= now
                now = divisor
                ans += bit
                bit = 1
            else:
                bit <<= 1
                now <<= 1
           
        if flag1^flag2 == 1:
            ans = -ans
            
        return min(max(-2147483648, ans), 2147483647)


# Driver
dividend = 10
divisor = 3

s = MySolution()
print(s.divide(dividend, divisor))