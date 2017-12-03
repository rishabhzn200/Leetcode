"""
283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        listIndex = 0
        numListLength = len(nums)
        for index in range(0,numListLength):
            if nums[index] != 0:
                nums[listIndex] = nums[index]
                listIndex += 1

        for index in range(listIndex, numListLength):
            nums[index] = 0

        pass

Solution().moveZeroes([0, 1, 0, 3, 12])