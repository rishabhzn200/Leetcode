"""
217. Contains Duplicate
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears
at least twice in the array, and it should return false if every element is distinct.
"""


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dupDict = {}
        for num in nums:
            try:
                dupDict[num] += 1
                return True
            except:
                dupDict[num] = 1
        return False

print(Solution().containsDuplicate([1,2,3,4,5,5]))