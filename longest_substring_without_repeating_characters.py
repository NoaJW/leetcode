# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class MySolution:
    def lengthOfLongestSubstring(self, s):
        substring = []
        max_count = 0
        starting_index = 0

        # start loop from each char to the end of string
        while starting_index <= (len(s) - 1): 
            # use enumerate to get the current index 
            for index, char in enumerate(s[starting_index:]):
                # if char does not exists in the substring array, insert it
                if substring.count(char) == 0:
                    substring.append(char)

                    if len(substring) > max_count: 
                        max_count = len(substring)

                    # if char is the last element, clear the substring array for the next loop (in while loop), and increment the starting_index to start loop from the next char 
                    if index == (len(s[starting_index:]) - 1): 
                        starting_index += 1
                        substring.clear()
                else: 
                    # if char exists in substring array, clear the array and insert it to begin a new substring 
                    substring.clear()
                    substring.append(char)

                    if len(substring) > max_count:  
                        max_count = len(substring)

                    if index == (len(s[starting_index:]) - 1): 
                        starting_index += 1
                        substring.clear()

        return max_count


# Driver
s = "abcabcbb"

sol = MySolution()
print(sol.lengthOfLongestSubstring(s))