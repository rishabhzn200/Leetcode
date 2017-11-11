class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index, element in enumerate(nums):
            if target - element in dict.keys():
                return [dict[target-element],(index)]
            else:
                dict[element] = index

print(str(Solution().twoSum([3,2,4], 6)))