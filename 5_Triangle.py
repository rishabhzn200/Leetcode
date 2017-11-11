
def  minSumTriangle(triangle):

    row = triangle.__len__()            #row index starts from 0 and ends at triangle.__len__() - 1
    col = triangle[row-1].__len__()     #col index starts from 0 and ends at triangle[row-1].__len__() - 1


    #Here we will start from 2nd last row and in each coloumn of 2nd last row we will store the min of triangle[row][col] + triangle[row+1][col] or triangle[row][col] + triangle[row+1][col+1].
    #After completing the 2nd last row we will move up and do the same thing with 3rd last row.
    #This continues till we reach the first row having only one element.
    #This element is returned. It contains the minimum sum.

    #Here oneUp variable is used to move one row up in the triangle array.

    oneUp = -1
    for rowIndex in range(row-2, -1, -1):
        oneUp += 1
        for columnIndex in range(0, col-1-oneUp, 1):
            triangle[rowIndex][columnIndex] += min(triangle[rowIndex+1][columnIndex], triangle[rowIndex+1][columnIndex+1])

    return triangle[0][0]


if __name__ == "__main__":

    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]

    x = minSumTriangle(triangle)
    print(x)
