# Problem: https://leetcode.com/problems/unique-number-of-occurrences/

# My solution
class MySolution:
    def uniqueOccurrences(self, arr):
        unique_items = []
        count = []
    
        for item in arr:
            if item not in unique_items:
                unique_items.append(item)
            
        for item in unique_items:
            item_count = arr.count(item)
            count.append(item_count)

        for c in list(count):
            count.remove(c)
      
            if c in count:
                return False  
            else:
                continue
            
        return True


class Solution:
    def uniqueOccurrences(self, arr):
        occurs = {}     # dict

        for num in arr:
            occurs[num] = occurs.get(num, 0) + 1     # create a counter for each item, put in a dict
         
        return len(set(occurs.values())) == len(occurs.values())  # convert to a set to remove duplicate items. Check if occurs has all unique values


# Driver
arr = [1,2,2,1,1,3]

s = MySolution()
print(s.uniqueOccurrences(arr))