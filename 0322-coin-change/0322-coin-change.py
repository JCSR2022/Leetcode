class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        
        min_coins = [amount + 1] * (amount + 1)
        min_coins[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    min_coins[i] = min(min_coins[i], 1 + min_coins[i - c])
        
        return min_coins[-1] if min_coins[-1] != amount + 1 else -1


#-------------------------------------------------------------------
        # N_coins = len(coins)

        # if amount == 0:
        #     return 0
        # my_memory = {}
        # def backtrack(coin_idx,coin_cnt,amount_left):

        #         if (coin_idx,coin_cnt,amount_left) in my_memory:
        #             return my_memory[(coin_idx,coin_cnt,amount_left)]

        #         if coin_idx == N_coins:
        #             return float("inf")

        #         if amount_left == 0:
        #             return coin_cnt
        #         #use coin 
        #         op1 = float("inf")
        #         if amount_left - coins[coin_idx] >= 0:
        #             op1 = backtrack(coin_idx,coin_cnt+1,amount_left-coins[coin_idx])
                
        #         #no use:
        #         op2 = backtrack(coin_idx+1,coin_cnt,amount_left)

        #         my_memory[(coin_idx,coin_cnt,amount_left)] = min(op1,op2)
        #         return my_memory[(coin_idx,coin_cnt,amount_left)] 
        
        # ans = backtrack(0,0,amount)

        # return ans if ans < float("inf") else -1 




#-------------------------------------------------------------------
        # if amount == 0:
        #     return 0

        # my_memory = {}
        # def backtrack(coin_cnt,amount_left):

        #     if (coin_cnt,amount_left) in my_memory:
        #         return my_memory[(coin_cnt,amount_left)]

        #     posibles_ans = [float("inf")]
        #     for coin_amount in coins:
        #         if coin_amount <= amount_left:
        #             next_amount = amount_left-coin_amount
        #             if next_amount == 0:
        #                 posibles_ans.append(coin_cnt+1)
        #             elif next_amount > 0 :
        #                 posibles_ans.append( backtrack(coin_cnt+1,next_amount) )

        #     my_memory[(coin_cnt,amount_left)] = min(posibles_ans)
        #     return my_memory[(coin_cnt,amount_left)]

        # ans = backtrack(0,amount)

        # return ans if ans < float("inf") else -1 
#Memory Limit Exceeded????????


#-------------------------------------------------------------------------
        # min_coin = min(coins)

        # if amount == 0:
        #     return 0

        # my_memory = {}
        # def backtrack(coin_cnt,amount_left):

        #     if (coin_cnt,amount_left) in my_memory:
        #         return my_memory[(coin_cnt,amount_left)]

        #     posibles_ans = [float("inf")]
        #     for coin_amount in coins:
        #         if coin_amount <= amount_left:
        #             coin_use = amount_left//coin_amount
        #             next_amount = amount_left%coin_amount 

        #             if next_amount == 0:
        #                 posibles_ans.append(coin_cnt+coin_use)
        #             elif next_amount == min_coin :
        #                 posibles_ans.append(coin_cnt+coin_use+1)
        #             elif next_amount > min_coin :
        #                 posibles_ans.append( backtrack(coin_cnt+coin_use,next_amount) )

        #     my_memory[(coin_cnt,amount_left)] = min(posibles_ans)
        #     return my_memory[(coin_cnt,amount_left)]

        # ans = backtrack(0,amount)

        # return ans if ans < float("inf") else -1 
#no esta bien, por ejemplo 11, con [5,2] devuelve -1, debe devolver 4


#--------------------------------
#         #y al menos intenta backtrack 17/08/2025

#         if amount == 0:
#             return 0

#         my_memory = {}
#         def backtrack(coin_cnt,curr_amount):

#             if (coin_cnt,curr_amount) in my_memory:
#                 return my_memory[(coin_cnt,curr_amount)]

#             if curr_amount == amount:
#                 return coin_cnt

#             if curr_amount > amount:
#                 return float("inf")

#             posibles_ans = []
#             for coin_amount in coins:
#                 posibles_ans.append(backtrack(coin_cnt+1,curr_amount+coin_amount))

#             my_memory[(coin_cnt,curr_amount)] = min(posibles_ans)
#             return my_memory[(coin_cnt,curr_amount)]

#         ans = backtrack(0,0)

#         return ans if ans < float("inf") else -1 


# #Memory Limit Exceeded
#-------------------------------------------------------------


















        #Aproach dp ....
        # Bottom up 
        # calculate te minim quantity of coins for to add 0,1,2,3.. until amunt
        # coins = [1,3,4,5]  amount =7
        #  dp[0] = {1:0,3:0,4:0,5:0}
        #  dp[1] = {1:1,3:0,4:0,5:0}
        #  dp[2] = {1:2,3:0,4:0,5:0}
        #  dp[3] = {1:0,3:1,4:0,5:0}
        #  dp[4] = {1:0,3:0,4:1,5:0}
        #  dp[5] = {1:0,3:0,4:0,5:1}
        #  dp[6] = {1:1,3:1,4:0,5:1}
        #  dp[7] = {1:0,3:1,4:1,5:0} = dp[4] +1?? 
        
        # if amount == 0:
        #     return 0 
        # dp = [float("inf"),{c:0 for c in coins}] * (amount+1)
        # dp[0] = [0,{c:0 for c in coins}]
        
        
        # for a in range(1, amount+10):
        #     print(dp)        
        #     print()
        #     for c in coins:
        #         if a - c >= 0:
        #             if dp[a][0] > 1 + dp[a-c][0]:
        #                 dp[a][0] = 1 + dp[a-c][0]
        #                 dp[a][1][c] += 1
                        
            
            
        # return 0
        
        
        


    
#[1,2,5,10,20,50,100,200,500,1000]
# 5848 -> 13
        
        
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
        #  dp[6] = 1 + Dp[5] = 2
        #  dp[7] = 1 + Dp[4] = 2
                

        
        
        # if amount == 0:
        #     return 0 
        
        # dp = [ float("inf")] * (amount + 1 )
        # dp[0] = 0
        
        # for a in range(1,amount + 1):
        #     print(dp)
        #     for c in coins:
        #         if a - c >= 0:
        #             dp[a] = min(dp[a], 1  + dp[a-c])
        # print(dp)
        # return dp[amount] if dp[amount] !=  float("inf") else -1
        
        
        
        
        
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
                    

        
    
        