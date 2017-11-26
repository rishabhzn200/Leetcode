class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        currPower = 0
        twoPowerCurrpower = 1 #2^0
        numOnes = 0

        bitList = [0]

        for i in range(1, num+1):

            if i == (twoPowerCurrpower * 2):
                currPower += 1
                twoPowerCurrpower *= 2
                numOnes = 0

            bitList.append(bitList[numOnes]+1)
            numOnes+=1

        return bitList




print(Solution().countBits(16))

