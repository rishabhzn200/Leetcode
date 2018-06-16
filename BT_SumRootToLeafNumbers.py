"""
129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def findSumRootToLeaf(root, totalSum, digList):
            if root is None:
                return totalSum

            digList.append(root.val)

            if root.left == None and root.right == None:
                listSum = int("".join([chr(x + 48) for x in digList]))
                del digList[-1]
                return totalSum + listSum

            totalSum = findSumRootToLeaf(root.left, totalSum,  digList)

            totalSum = findSumRootToLeaf(root.right,totalSum,  digList)

            del digList[-1]

            return totalSum


        newSum = findSumRootToLeaf(root, 0,  [0])
        return newSum

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

print(Solution().sumNumbers(root))