class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        left = 0
        right = 1
        profit = max(0, prices[right] - prices[left])

        while left < len(prices) and right < len(prices):
            print(left, right)
            if prices[right] <= prices[left]:
                left = right
                right += 1
            else:
                profit = max(profit, prices[right] - prices[left])
                right += 1
        
        return profit
