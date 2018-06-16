
"""
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers
along its path.
"""

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        minPathGrid = grid[:]

        for col in range(1,len(minPathGrid[0])):
            minPathGrid[0][col] += minPathGrid[0][col-1]

        for row in range(1, len(minPathGrid)):
            minPathGrid[row][0] += minPathGrid[row-1][0]

        for row in range(1,len(minPathGrid)):
            for col in range(1,len(minPathGrid[0])):
                minPathGrid[row][col] += min(minPathGrid[row-1][col], minPathGrid[row][col-1])

        return minPathGrid[len(minPathGrid)-1][len(minPathGrid[0])-1]




if __name__ == "__main__":
    costMatrix  =   [[1,3,1],
                    [1,5,1],
                    [4,2,1]]
    cost = costMatrix[:]
    minimumPath = Solution().minPathSum(cost)
    print(minimumPath)