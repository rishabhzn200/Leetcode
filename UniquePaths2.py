"""
63. Unique Paths II

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # create a m*n table to store the dp values
        table = [[0 for x in range(n)] for y in range(m)]

        # path to any col in row 1 is always 1
        for col in range(n):
            if obstacleGrid[0][col] == 0:
                table[0][col] = 1
            else:
                break

        # path to any row in col 1 is always 1
        for row in range(m):
            if obstacleGrid[row][0] == 0:
                table[row][0] = 1
            else:
                break

        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] == 1:
                    table[row][col] = 0
                else:
                    table[row][col] = table[row - 1][col] + table[row][col - 1]

        return table[m-1][n-1]

grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

Solution().uniquePathsWithObstacles(grid)