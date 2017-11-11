


import sys
def maxCrossSum(nums, mid):

    sum = 0
    leftSum = -sys.maxsize  # very low value
    rightSum = -sys.maxsize  # very low value

    for i in range(mid, -1, -1):  # start from mid point and go upto 0 (including 0)
        sum += nums[i]
        if sum > leftSum:
            leftSum = sum

    sum = 0
    for i in range(mid + 1, nums.__len__(), 1):
        sum += nums[i]
        if sum > rightSum:
            rightSum = sum

    totalCrossSum = leftSum + rightSum
    return totalCrossSum

    pass

def maxSubArray(nums):

    n = nums.__len__()

    if n == 1:
        return nums[0]

    # Divide the problem in to subproblem
    mid = int(n / 2)

    l = maxSubArray(nums[:mid])  # we are passing the divided array instead of passing array and its low and high value, so indexing will be from 0 - n-1 always
    r = maxSubArray(nums[mid:])
    lr = maxCrossSum(nums, mid - 1)

    return max(l, r, lr)

#testing the solution
print("Max Subarray Sum is: " + str(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])))