class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        pointer_1 = 0
        profit = 0
        actual_profit = 0

        for pointer_2 in range(1,size):
            
            if prices[pointer_2] > prices[pointer_2-1] :
                actual_profit = prices[pointer_2] - prices[pointer_1]
            else:
                pointer_1 = pointer_2
                profit += actual_profit
                actual_profit = 0
            
        return profit + actual_profit

        