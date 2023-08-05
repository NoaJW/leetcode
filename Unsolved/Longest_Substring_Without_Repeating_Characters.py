# class MySolution:
#     def lengthOfLongestSubstring(self, s: str):
#         substr = []
#         substr2 = []

#         for counter1, item1 in enumerate(s):
#             substr.append(item1)

#             for counter2, item2 in enumerate(s):
#                 print("count1: ", counter1)
#                 print("count2: ", counter2)

#                 if counter1 != counter2:
#                     if item1 == item2: 
#                         substr2.append(item2)
#                     else: 
               
#                         substr.append(item2)
                    
#                 if len(substr2) > len(substr):
#                     substr = substr2.copy()
#                     substr2.clear()

#                 print("substr: ", substr)
#                 print("substr2: ", substr2)
                        
#         return substr

# s = MySolution()
# print(s.lengthOfLongestSubstring("skeske"))

class Solution:
    def lengthOfLongestSubstring(self, s: str):
        last_seen = {}
        start = 0
        longest = 0

        for counter, item in enumerate(s):
            if item in last_seen and last_seen[item] >= start:
                start = last_seen[item] + 1
            else:
                longest = max(longest, counter - start + 1)
            
            last_seen[item] = counter
        return longest

# s = Solution()
# print(s.lengthOfLongestSubstring("skefaske"))

                