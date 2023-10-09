# class Solution:
#     def countAndSay(self, n):
#         # for i in range(1, n+1):
#         seq = ['1']
#         char_set = []
#         counter = 0
#         counter_char = []

#         for index in range(n):
#             char_set.append(seq[-1][0])
#             for char in seq[-1]:
#                 if char == char_set[0]:
#                     counter += 1
                    
#                 else:
                    
#                     char_set[0] = char
#                     counter = 1
                
#                 counter_char.append(char, counter)
                         


#             # seq.append()           

