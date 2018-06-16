"""
61. Rotate List

Given a list, rotate the list to the right by k places, where k is non-negative.


Example:

Given 1->2->3->4->5->NULL and k = 2,

return 4->5->1->2->3->NULL.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head == None or head.next == None or k == 0:
            return head

        c = 0

        x = head
        prevL1 = None
        while True:
            c += 1

            if x.next == None:
                x.next = head
                prevL1 = x
                break
            x = x.next

        if k > c:
            k = k % c

        l1 = head

        prev = prevL1

        while k != 0:
            prevL1 = l1
            l1 = l1.next
            k -= 1

        curr = head

        while l1 != head:
            prev = curr
            curr = curr.next
            l1 = l1.next

        head = curr
        prev.next = None

        return head
    