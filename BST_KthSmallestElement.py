"""
230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """



        def traverse(root, k, curr):

            if root == None:
                return curr

            curr = traverse(root.left, k, curr)

            curr = curr + 1
            if curr == k:
                return curr

            curr = traverse(root.right, k)
            if curr == k:
                return curr

            return curr

        traverse(root, k, 0)