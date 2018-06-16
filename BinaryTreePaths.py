"""
257. Binary Tree Paths
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def traverse(root, currPath):

            if root == None:
                return None

            currPath.append(root.val)

            lc = traverse(root.left, currPath)

            rc = traverse(root.right, currPath)

            if lc == None and rc == None:
                traverse.pathList.append(currPath[:])

            del currPath[-1]
            return root

        traverse.pathList = []
        traverse(root, [])

        pathStringList = []
        for paths in traverse.pathList:
            pathString = ""
            for index, node in enumerate(paths):
                if index == 0:
                    pathString = str(node)
                else:
                    pathString = pathString + "->" + str(node)

            pathStringList.append(pathString)


        return pathStringList

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.right.right = TreeNode(11)

root.left.left = TreeNode(3)
root.left.right = TreeNode(2)

root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)

root.left.right.right = TreeNode(1)

cnt = Solution().binaryTreePaths(root)

print(cnt)

c = 20