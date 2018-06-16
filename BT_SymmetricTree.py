"""
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        def symmetric(rootL, rootR):

            if rootL == None and rootR == None:
                return True

            if rootL == None or rootR == None:
                return False


            left = False
            right = False
            if rootL.val == rootR.val:
                left = symmetric(rootL.left, rootR.right)
                right = symmetric(rootL.right, rootR.left)
                return left and right

            return False

        return symmetric(root.left, root.right)

