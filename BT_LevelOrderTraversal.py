"""
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        bftList = []
        q1 = [root, None]

        nodeListInSameLevel = []
        while True:
            if len(q1) == 0:
                break

            x = q1.pop(0)

            if x == None:
                if len(q1) != 0:
                    q1.append(None)
                bftList.append(nodeListInSameLevel[:])
                nodeListInSameLevel = []


            else:
                nodeListInSameLevel.append(x.val)
                if x.left != None:
                    q1.append(x.left)
                if x.right != None:
                    q1.append(x.right)


        return bftList


