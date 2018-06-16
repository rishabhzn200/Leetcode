
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if len(matrix) == 0:
            return []
        row = len(matrix)
        col = len(matrix[0])

        rowStart = 0
        rowEnd = row - 1
        colStart = 0
        colEnd = col - 1

        mat = []

        while ((rowStart <= rowEnd) and (colStart <= colEnd)):

            for c in range(colStart, colEnd + 1):
                mat.append(matrix[rowStart][c])

            rowStart += 1

            for k in range(rowStart, rowEnd+ 1):
                mat.append(matrix[k][colEnd])

            colEnd -= 1

            if rowStart <= rowEnd:
                for j in range(colEnd, colStart - 1, -1):
                    mat.append(matrix[rowEnd][j])

                rowEnd -= 1

            if colStart <= colEnd:
                for l in range(rowEnd, rowStart, -1):
                    mat.append(matrix[l][colStart])

                colStart += 1

        return mat


# matrix = [
#  [ 1, 2, 3, 4 ],
#  [ 10, 11, 12, 5 ],
#  [ 9, 8, 7, 6 ]
# ]

# matrix = [
#  [ 1,   2, 3 ],
#  [ 10, 11, 4 ],
#  [ 9,  12, 5 ],
#  [ 8,   7, 6]
# ]

matrix = [
    [1,2,3],
    [8,9,4],
    [7,6,5]

]

print(Solution().spiralOrder(matrix))