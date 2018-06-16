"""
77. Combinations
DescriptionHintsSubmissionsDiscussSolution
DiscussPick One
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        allCombination = []
        incExc = []

        def combination(n, start, end, k, incExc):

            if start == end:
                newComb = []
                numSelected = sum(1 for y in incExc if y == 1)

                if numSelected == k:
                    for i in range(n):
                        if incExc[i] == 1:
                            newComb.append(i+1)

                    allCombination.append(newComb)

                return

            for j in range(0,2):
                incExc.append(j)
                combination(n, start+1, end, k, incExc)
                del incExc[-1]

            pass

        combination(n, 0, n, k, incExc)

        return allCombination



print(Solution().combine(20,16))