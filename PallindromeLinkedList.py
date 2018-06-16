"""
234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        def isLLPallindrome(head):

            if head == None:
                return

            isLLPallindrome(head.next)
            isLLPallindrome.palList.append(head.val)

        isLLPallindrome.palList = []
        isLLPallindrome(head)

        index = 0
        while head is not None:
            if isLLPallindrome.palList[index] != head.val:
                return False
            index += 1
            head = head.next
        return True

head = ListNode(10)
head.next = ListNode(9)
head.next.next = ListNode(10)

print(Solution().isPalindrome(head))