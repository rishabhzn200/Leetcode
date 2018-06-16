# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        s = []
        def traverse(root):
            if root is None:
                s.append("None")
                return
            else:
                s.append(root.val)
                traverse(root.left)
                traverse(root.right)
        traverse(root)
        return s




    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        index = 0


        def disel(index):
            if index >= len(data):
                return None
            if data[index] == "None":
                return None
            else:
                root = TreeNode(data[index])
                root.left = disel(index + 1)
                root.right = disel(index + 2)
            return root

        index = 0
        head = disel(index)
        return head


        pass



root = TreeNode(2)
root.left              = TreeNode(8)
root.right              = TreeNode(6)
# root.left.left         = TreeNode(4)
# root.left.right        = TreeNode(12)
# root.left.right.left   = TreeNode(10)
# root.left.right.right  = TreeNode(14)

# Your Codec object will be instantiated and called as such:
codec = Codec()
s = codec.serialize(root)
ds = codec.deserialize(s)
n = 20
