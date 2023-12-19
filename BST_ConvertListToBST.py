"""
109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None:
            return None

        if head.next == None:
            return TreeNode(head.val)

            # slow, fast = None, None

            # if head.next.next == None:
            #     slow = head
            #     fast = head.next.next

        slow, fast = head, head.next.next

        while fast and fast.next:
            slow = slow.next
            if fast := fast.next:
                fast = fast.next

        r = slow.next
        slow.next = None

        root = TreeNode(r.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(r.next)
        return root

#[-10,-3,0,5,9]

head = ListNode(-10)
head.next = ListNode(-3)
head.next.next = ListNode(0)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)

Solution().sortedListToBST(head)
