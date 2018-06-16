"""
17. Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters is just like on the telephone buttons.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        possibleStrings = []

        mapping = {"0":" ", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz", "1":"" }

        newstr = ""

        def mapdigit2letter(str, start, end, newstr):

            if start == end:
                if newstr != "":
                    possibleStrings.append(newstr[:])
                return
                pass

            for possibleLetter in mapping[str[start]]:
                oldstr = newstr
                newstr = newstr + possibleLetter
                mapdigit2letter(str, start + 1, end, newstr)
                newstr = oldstr


            pass

        mapdigit2letter(digits, 0, len(digits), newstr)
        return possibleStrings


print(Solution().letterCombinations(""))