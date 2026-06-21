class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:


        # heapCream_prices = [(price,cnt) for price,cnt in Counter(costs).items()]
        # heapq.heapify(heapCream_prices)
        # #print("heapCream_prices:",heapCream_prices)

        # ans = 0
        # while heapCream_prices and coins > 0:
        #     curr_price,curr_cnt = heapq.heappop(heapCream_prices)
        #     #print("curr_price,curr_cnt :",curr_price,curr_cnt )
    
        #     if curr_price*curr_cnt <= coins:
        #         ans += curr_cnt
        #         coins -= curr_price*curr_cnt
        #     else:
        #         ans += coins//curr_price
        #         return ans

        # return ans        

#---------------------------------------------------------------------------

        max_cost = max(costs)
        freq = [0] * (max_cost + 1)
        for cost in costs:
            freq[cost] += 1
        
        count = 0
        for price in range(1, max_cost + 1):
            if freq[price] == 0:
                continue
            if coins < price:
                break
            can_buy = min(freq[price], coins // price)
            count += can_buy
            coins -= can_buy * price
        
        return count