"""
Word Search:

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

"""


class Solution:

    def __init__(self):
        pass


    def dfs(self, board, word, row, col, index=0):

        if row<0 or col<0 or row>=board.__len__() or col>=board[0].__len__():
            return False

        if board[row][col] == word[index]:



            if index == word.__len__()-1:
                return True

            #Call dfs in recursive fashion
            #mark it as visited. 2 Ways: 1. keep a dummy value within the original 2d array. or 2. Create a separate array
            visited = board[row][col]
            board[row][col] = 1

            up    = self.dfs(board, word, row - 1, col, index + 1)
            down  = self.dfs(board, word, row + 1, col, index + 1)
            left  = self.dfs(board, word, row    , col - 1, index + 1)
            right = self.dfs(board, word, row    , col + 1, index + 1)

            if(left==True or right == True or up == True or down == True):
                return True

            board[row][col] = visited

        return False





        pass

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        wsList = [[i,j] for i,row in enumerate(board) for j, col in enumerate(board[i]) if word[0] == board[i][j]]
        wordFound = False
        for eachws in wsList:
            #we found 1st matching letter. Find other letters using recursion
            if (wordFound := self.dfs(board, word, eachws[0], eachws[1])) == True:
                return True

        if wordFound == False:
            return False


board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

print(Solution().exist(board, "EEDA"))
