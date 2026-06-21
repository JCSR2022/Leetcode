class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:


        heapCream_prices = [(price,cnt) for price,cnt in Counter(costs).items()]
        heapq.heapify(heapCream_prices)
        #print("heapCream_prices:",heapCream_prices)

        ans = 0
        while heapCream_prices and coins > 0:
            curr_price,curr_cnt = heapq.heappop(heapCream_prices)
            #print("curr_price,curr_cnt :",curr_price,curr_cnt )
    
            if curr_price*curr_cnt <= coins:
                ans += curr_cnt
                coins -= curr_price*curr_cnt
            else:
                ans += coins//curr_price
                return ans

        return ans        