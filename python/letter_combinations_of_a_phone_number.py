# Problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# My solution
from itertools import product

class MySolution:
    def letterCombinations(self, digits: str):
        if len(digits) == 0: 
            return []
        
        num_alphabets = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'], "5": ['j', 'k', 'l'], "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'], "8": ['t', 'u', 'v'], "9": ['w', 'x', 'y', 'z']}      

        # get all list values of digits, encapsulate in a list 
        to_combine_lists= [num_alphabets[digit] for digit in digits if digit in num_alphabets]

        # Get all paired combinations from the lists as tuples, join them as strings and encapsulate in a list  
        combinations = ["".join(combination) for combination in product(*to_combine_lists)]

        return combinations


# Driver
digits = ""

s = MySolution()
print(s.letterCombinations(digits))
