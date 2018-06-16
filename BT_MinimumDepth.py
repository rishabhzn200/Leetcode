"""
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

            # if root.left == None and root.right == None:
            #     return 1

        leftMin = self.minDepth(root.left)
        rightMin = self.minDepth(root.right)

        if leftMin == 0:
            return 1 + rightMin
        if rightMin == 0:
            return 1 + leftMin

        return 1 + min(leftMin, rightMin)
