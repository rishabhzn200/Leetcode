class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        if len(prices) == 2:
            if prices[0] < prices[1]:
                return prices[1] - prices[0]
            else:
                return 0

        max_profit = prices[1] - prices[0]
        min_ind = 0

        for i in range(1, len(prices)):
            newProfit = prices[i] - prices[min_ind]
            max_profit = max(newProfit, max_profit)
            if prices[i] < prices[min_ind]:
                min_ind = i

        #If max_profit is negative dont sell the stocks. In that case, max_profit = 0
        max_profit = max(max_profit, 0)
        return max_profit

print(Solution().maxProfit([7,6,5]))