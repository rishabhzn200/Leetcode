"""
162. Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return 0  # index to be returned

        l = 0
        h = len(nums)-1
        mid = 0
        while l <= h:
            mid = int((l + h) / 2)

            if mid == h or mid == l:
                if h != l:
                    if nums[l] > nums[h]:
                        mid = l
                    else:
                        mid = h
                break
            if nums[mid] < nums[mid + 1]:
                l = mid
            elif nums[mid] < nums[mid - 1]:
                h = mid
            else:
                break

        return mid


print(Solution().findPeakElement([1,2,3,4,5]))