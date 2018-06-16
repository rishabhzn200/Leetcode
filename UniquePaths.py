"""
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        #create a m*n table to store the dp values
        table = [[0 for x in range(n)] for y in range(m)]

        #path to any col in row 1 is always 1
        for col in range(n):
            table[0][col] = 1

        #path to any row in col 1 is always 1
        for row in range(m):
            table[row][0] = 1


        for row in range(1,m):
            for col in range(1,n):
                table[row][col] = table[row-1][col] + table[row][col-1]

        return table[m-1][n-1]


Solution().uniquePaths(3,4)