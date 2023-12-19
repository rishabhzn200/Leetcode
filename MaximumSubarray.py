import sys
class Solution:
    def maxCrossSum(self, nums, mid):

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

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if (n := nums.__len__()) == 1:
            return nums[0]

        # Divide the problem in to subproblem
        mid = int(n / 2)

        l = self.maxSubArray(nums[:mid])  # we are passing the divided array, so indexing will be from 0 - n-1 always
        r = self.maxSubArray(nums[mid:])
        lr = self.maxCrossSum(nums, mid - 1)

        return max(l, r, lr)

print("Max Subarray Sum is: " + str(Solution().maxSubArray([-1,-2,10,4,2,-1,2,3])))
