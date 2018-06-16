"""
46. Permutations

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permList = []

        def permutation(nums, start, end):

            if start == end:
                permList.append(nums[:])
                pass

            for i in range(start, end):
                nums[i], nums[start] = nums[start], nums[i]

                permutation(nums, start + 1, end)

                nums[i], nums[start] = nums[start], nums[i]

            pass

        permutation(nums, 0, len(nums))
        return permList


print(Solution().permute([1,2,3]))