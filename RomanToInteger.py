"""
13. Roman to Integer

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rtiDict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        sum = 0

        i = 0

        while i < len(s):
            curr = rtiDict[s[i]]

            if (i+1) < len(s):

                next = rtiDict[s[i+1]]

                if curr >=next:
                    sum += curr
                else:
                    sum = sum - curr + next
                    i += 1
            else:
                sum += curr
                i += 1
            i += 1
        return sum

print(Solution().romanToInt("MCMIV"))


