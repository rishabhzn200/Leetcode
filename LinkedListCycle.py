"""
141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False

        p1 = head
        p2 = head.next
        while p1 != None and p2 != None:
            if p1 == p2:
                return True

            p1 = p1.next
            p2 = p2.next
            if p2 == None:
                return False
            p2 = p2.next
        return False
    