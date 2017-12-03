"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        temp = None
        c = 0
        while l1 != None and l2 != None:
            s = l1.val + l2.val + c
            x = s % 10
            c = int(s / 10)
            if head == None:
                head = ListNode(x)
                temp = head
            else:
                temp.next = ListNode(x)
                temp = temp.next

            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            s = l1.val + c
            x = s % 10
            c = int(s / 10)

            if head == None:
                head = ListNode(x)
                temp = head
            else:
                temp.next = ListNode(x)
                temp = temp.next
            l1 = l1.next

        while l2 != None:
            s = l2.val + c
            x = s % 10
            c = int(s / 10)

            if head == None:
                head = ListNode(x)
                temp = head
            else:
                temp.next = ListNode(x)
                temp = temp.next
            l2 = l2.next

        if c > 0:
            temp.next = ListNode(c)
            temp = temp.next

        return head