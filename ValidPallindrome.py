"""
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        import re
        qry = re.compile(r'[A-Za-z0-9]')
        m = qry.findall(s)
        r = [m[x] for x in range(len(m)-1, -1, -1)]

        if m==r:
            return True
        return False


string = "A man, a plan, a canal: Panam"

Solution().isPalindrome(string)