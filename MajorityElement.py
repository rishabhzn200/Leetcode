"""
169. Majority Element
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums) >> 1
        numFreqDict = {}
        for num in nums:
            try:
                numFreqDict[num] += 1
            except:
                numFreqDict[num] = 1

            if numFreqDict[num] > l:
                return l

print(Solution().majorityElement([1]))