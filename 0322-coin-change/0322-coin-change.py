class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        #Aproach dp ....
        # Bottom up 
        # calculate te minim quantity of coins for to add 0,1,2,3.. until amunt
        # coins = [1,3,4,5]  amount =7
        #  dp[0] = 0
        #  dp[1] = 1
        #  dp[2] = 1 +dp[1] = 2
        #  dp[3] = 1
        #  dp[4] = 1
        #  dp[5] = 1
        #  dp[6] = 2
        #  dp[7] = 2
        
        if amount == 0:
            return 0 
        
        dp = [ float("inf")] * (amount + 1 )
        dp[0] = 0
        
        for a in range(1,amount + 1):
            #print(dp)
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1  + dp[a-c])
        
        return dp[amount] if dp[amount] !=  float("inf") else -1
            
            
        
        
        
        
        
        
        
        
#           greedy Noooo, 
#           dfs... aproach ??.... 
        
        
#         if amount == 0:
#             return 0
        
#         cont = 1
#         sumCoins = set(coins)
        
#         while min(sumCoins) <= amount :
#             print(sumCoins)
#             if amount in sumCoins:
#                 return cont
            
#             next_sumCoins = set()
#             for s_co in sumCoins:
#                 for c in coins:  
#                     next_sumCoins.add(s_co+c)
#             sumCoins = next_sumCoins
#             cont+= 1
            
#         return -1
                    

        
    
        