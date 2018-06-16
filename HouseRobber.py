"""
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob
tonight without alerting the police.
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return nums[0]

        if l == 2:
            return max(nums[0], nums[1])

        money = [0]*l
        money[0] = nums[0]
        money[1] = nums[1]

        for i in range(2,l):
            money[i] = max(nums[i]+money[i-2], money[i-1])

        return money[-1]