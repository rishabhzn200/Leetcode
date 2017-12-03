"""
268. Missing Number
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

"""


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum_0_to_N = int(n * (n+1)/2)
        sumOfList = sum(nums)
        return sum_0_to_N - sumOfList

print(Solution().missingNumber([0,1,3]))