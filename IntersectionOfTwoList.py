"""
160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numNodes(self, head):
        c = 0
        while head != None:
            c += 1
            head = head.next
        return c

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        c1 = self.numNodes(headA)
        c2 = self.numNodes(headB)

        if c1 == 0 or c2 == 0:
            return None
        l1 = headA
        l2 = headB

        if c1 > c2:
            for i in range(0, c1 - c2):
                l1 = l1.next

        elif c2 > c1:
            for i in range(0, c2 - c1):
                l2 = l2.next

        node = None
        while l1 != None and l2 != None:
            if l1 == l2:
                node = l1
                break
            l1 = l1.next
            l2 = l2.next
        return node
