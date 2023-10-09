# Problem: https://leetcode.com/problems/word-search/description/

# Solution
class MySolution:
   def exist(self, board, word):
        def dfs(board, word, i, j, k):      
            # If the position is out of the bounds of the grid, or the character does not match, return False
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            
            # Letter matched above, move to next adjacent space (up, down, left, right) 

            # If the last character matches (all letters matched), return True
            if k == len(word) - 1:
                return True
            
            # Save the current character and mark the cell as visited, so adjacent checks will return False for visited cell
            tmp, board[i][j] = board[i][j], '/'

            # Explore the neighboring cells
            res = dfs(board, word, i + 1, j, k + 1) or dfs(board, word, i - 1, j, k + 1) \
                or dfs(board, word, i, j + 1, k + 1) or dfs(board, word, i, j - 1, k + 1)
            
            # Restore the current character and backtrack
            board[i][j] = tmp

            return res


        for i in range(len(board)):
            for j in range(len(board[0])):      # Start from the first row only
                # Start the DFS search from each cell
                if dfs(board, word, i, j, 0):
                    return True
                
        return False


# Driver
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"

s = MySolution()
print(s.exist(board, word))


