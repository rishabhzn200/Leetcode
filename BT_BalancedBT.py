"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def balance(root):
            if root == None:
                return 0

            if root.left == None and root.right == None:
                return 1

            leftDepth = balance(root.left)
            rightDepth = balance(root.right)

            if leftDepth == -1 or rightDepth == -1 or abs(leftDepth - rightDepth) > 1:
                return -1

            return 1+ max(leftDepth, rightDepth)



        res = balance(root)
        if res != -1:
            return True
        return False


root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.right.right = TreeNode(3)

root.left.left.left = TreeNode(4)
root.right.right.right = TreeNode(4)


print(Solution().isBalanced(root))