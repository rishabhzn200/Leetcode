"""
113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSum(self, node, remsum, sumList, sumLists):
        if node == None:
            return

        if (node.val == remsum and node.left == None and node.right == None):
            sumList.append(node.val)
            sumLists.append(sumList[:])
            del sumList[-1]  # remove the newly added node
            return

        else:
            sumList.append(node.val)

            self.findSum(node.left, remsum - node.val, sumList, sumLists)
            self.findSum(node.right, remsum - node.val, sumList, sumLists)

            del sumList[-1]

        pass

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        if root == None:
            return []

        sumLists = []

        sumList = []
        self.findSum(root, sum, sumList, sumLists)

        return sumLists