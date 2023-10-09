# Problem: https://leetcode.com/problems/valid-palindrome/description/

# My solution
class MySolution:
    def isPalindrome(self, s: str) -> bool:
        my_str = "".join(filter(str.isalnum, s)).lower()     # Remove non-alphanumeric char and convert to lowercase
        
        return my_str == my_str[::-1]


# Driver
str = "A man, a plan, a canal: Panama"

s = MySolution()
print(s.isPalindrome(str))
