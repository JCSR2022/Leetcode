class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        #brute force:
        
        ans = []
        for i,price_i in enumerate(prices):
            j = i+1
            while j < len(prices):
                if prices[j] <= price_i:
                    ans.append(price_i-prices[j])
                    break
                else:
                    j +=1
            if j == len(prices):
                ans.append(price_i)
                
        return ans
            