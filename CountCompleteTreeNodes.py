"""
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level
are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def count(root, sum):
            if root == None:
                return sum

            if root.left == None and root.right == None:
                return 1 + sum

            sum = count(root.left, sum)

            sum = count(root.right, sum)

            #Add one for current node
            return sum + 1

        return count(root, 0)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)

print(Solution().countNodes(root))