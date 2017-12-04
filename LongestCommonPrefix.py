"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution:
    # @param {string[]} strs
    # @return {string}

    def lcp(self, strs, l, h):

        if l == h:
            return strs[l]

        if h > l:
            mid = int((l+h)/2)

            s1 = self.lcp(strs, l, mid)
            s2 = self.lcp(strs,mid+1,h)

            #find common in two
            min2l = min(len(s1), len(s2))
            c = ""
            for i in range(min2l):
                if s1[i] == s2[i]:
                    c += s1[i]
                else:
                    break
            return c


    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        l = 0
        h = len(strs)

        return self.lcp(strs, l, h-1)


print(Solution().longestCommonPrefix(["heart", "heavy", "heaven", "heavier"]))
