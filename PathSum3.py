
"""
437. Path Sum III
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def traverse(root, currSum):

            if root == None:
                return

            # currSum += root.val

            currSum.append(root.val)
            l = len(currSum)
            for index in range(0, l-1):
                currSum[index] += root.val

            for eachVal in currSum:
                if eachVal == sum:
                    traverse.count += 1

            traverse(root.left, currSum)



            traverse(root.right, currSum)

            for index in range(0, l-1):
                currSum[index] -= root.val

            del currSum[-1]



            pass

        traverse.count = 0
        traverse(root, [])
        return traverse.count


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.right.right = TreeNode(11)

root.left.left = TreeNode(3)
root.left.right = TreeNode(2)

root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)

root.left.right .right = TreeNode(1)

cnt = Solution().pathSum(root, 8)

print(cnt)

c = 20