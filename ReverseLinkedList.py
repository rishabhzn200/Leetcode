"""
206. Reverse Linked List
Reverse a singly linked list.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head

        temp = head.next
        newHead = self.reverseList(head.next)
        temp.next = head
        head.next = None
        return newHead