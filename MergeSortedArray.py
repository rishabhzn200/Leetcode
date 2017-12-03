"""
88. Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.

"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        indexNum1 = m-1
        indexNum2 = n-1

        while(indexNum1 >=0  and indexNum2 >= 0):

            #Move greater number to num2 array
            if nums1[indexNum1] > nums2[indexNum2]:
                nums1[indexNum1+indexNum2+1] =  nums1[indexNum1]
                indexNum1 -= 1
            else:
                nums1[indexNum1 + indexNum2 + 1] = nums2[indexNum2]
                indexNum2 -= 1

        while indexNum2 >= 0:
            nums1[indexNum2] = nums2[indexNum2]
            indexNum2 -= 1



num1 = [21,23]
num2 = [2,4,5,8,11,12]

num1len = len(num1)
num2len = len(num2)

#To satisfy initial problem condition
num1 = num1 + [0]*num2len

Solution().merge(num1, num1len, num2, num2len)













