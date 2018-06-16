"""
47. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permList = []

        def permute(nums, start, end):


            dict = {}

            if start == end:
                permList.append(nums[:])
                pass

            for i in range(start, end):

                try:
                    if dict[nums[i]] == 1:
                        continue
                except:
                    dict[nums[i]] = 1
                    nums[i], nums[start] = nums[start], nums[i]

                    permute(nums, start+1, end)

                    nums[i], nums[start] = nums[start], nums[i]


        permute(nums, 0, len(nums))
        return permList

print(Solution().permuteUnique([1,1,2]))