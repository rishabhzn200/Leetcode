
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        subsetList = []

        def findSubsets(nums, start, end, inSet):

            if start == end+1:
                newset = []
                indexes = [x for x in range(len(inSet)) if inSet[x] == 1]

                for index in indexes:
                    newset.append(nums[index])

                subsetList.append(newset)

                return

            for j in range(0,2):
                inSet[start] = j
                findSubsets(nums, start+1, end, inSet)



        inSet = [0]*len(nums)

        findSubsets(nums, 0, len(nums)-1, inSet)
        return subsetList


print(Solution().subsets([2,3,4]))