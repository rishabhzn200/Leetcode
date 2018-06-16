import binascii

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsetList = []

        l = 2**len(nums)
        for i in range(l):
            set = []
            x = str(bin(i))
            x = x[2:]
            x = '0'* (len(nums) - len(x)) + x
            for j in range(len(x)):
                if x[j] == '1':
                    set. append(nums[j])

            subsetList.append(set)

        return subsetList

Solution().subsets([2,3,4])
