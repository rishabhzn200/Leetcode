"""
19. Remove Nth Node From End of List

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.


"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        temp = ListNode(0)
        temp.next = head

        h2 = head
        nodeIndex = 1
        while nodeIndex <= n:
            h2 = h2.next
            nodeIndex += 1

        # check condition for h2 = None
        if h2 == None:
            if head == None:
                return []
            else:
                head = head.next
                return head

        while h2.next != None:
            head = head.next
            h2 = h2.next

        if head != None:
            head.next = head.next.next

        head = temp.next
        return head

head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

root = Solution().removeNthFromEnd(head, 1)

while root != None:
    print(root.val)
    root = root.next
