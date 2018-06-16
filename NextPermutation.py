"""
31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #Algorithm
        """
        Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
        Find the largest index l greater than k such that a[k] < a[l].
        Swap the value of a[k] with that of a[l].
        Reverse the sequence from a[k + 1] up to and including the final element a[n].
        """

        # flag = False
        # index = 0
        # for i in range(len(nums)-2, -1, -1):
        #     print(str(nums[i]) + "<" + str(nums[i+1]))
        #     if nums[i] < nums[i+1]:
        #         flag, index = True, i
        #         break
        #
        # if flag:
        #     #index found
        #     #return index
        #     swapIndex = -1
        #     for i in range(index+1, len(nums), 1):
        #         if nums[index] < nums[i]:
        #             swapIndex = i
        #
        #     nums[index], nums[swapIndex] = nums[swapIndex], nums[index]
        #
        #     p = nums[0:index+1]
        #     q = [x for x in reversed(nums[index+1:])]
        #
        #
        #     b = nums[0:index+1] + [x for x in reversed(nums[index+1:])]
        #     nums = b
        #     return nums
        #
        # else:
        #     return [x for x in reversed(nums)]

        flag = False
        index = 0
        for i in range(len(nums) - 2, -1, -1):
            # print(str(nums[i]) + "<" + str(nums[i+1]))
            if nums[i] < nums[i + 1]:
                flag, index = True, i
                break

        if flag:
            # index found
            # return index
            swapIndex = -1
            for i in range(index + 1, len(nums), 1):
                if nums[index] < nums[i]:
                    swapIndex = i

            nums[index], nums[swapIndex] = nums[swapIndex], nums[index]

            p = nums[0:index + 1]
            q = [x for x in reversed(nums[index + 1:])]

            for i in range(int((len(nums) - index - 1) / 2)):
                nums[index + 1 + i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[index + 1 + i]

        else:
            for i in range(0, int((len(nums)) / 2)):
                nums[i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[i]

        return nums

print(Solution().nextPermutation([100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69,68,67,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]))