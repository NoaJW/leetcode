# Problem: https://leetcode.com/problems/length-of-last-word/

# My solution
class MySolution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        counter = 0 

        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                break

            counter += 1

        return counter
        
        
# Driver
str = "   fly me   to   the moon  "

s = MySolution()
print(s.lengthOfLastWord(str))