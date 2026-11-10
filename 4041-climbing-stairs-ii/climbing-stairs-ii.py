class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:


        #try dfs with memo, if not have to be dp

        # mymemo = {}
        # def dfs(step,curr_cost):
        #     if step == n:
        #         return curr_cost

        #     if (step,curr_cost) in mymemo:
        #         return mymemo[(step,curr_cost)]

            
        #     opc1 = dfs(step+1,curr_cost+costs[step]+1)
        #     opc2 = dfs(step+2,curr_cost+costs[step+1]+4) if step+2 <= n else float("inf") 
        #     opc3 = dfs(step+3,curr_cost+costs[step+2]+9) if step+3 <= n else float("inf") 

        #     mymemo[(step,curr_cost)] = min(opc1,opc2,opc3)
        #     return mymemo[(step,curr_cost)]
            
        # return dfs(0,0)

#Memory Limit Exceeded
#------------------------------------------------------


        #dp

        # dp = [float("inf")]*n

        # dp[0] = 0
    
        # dp[1] = costs[0] + 1
        # if n == 1:
        #     return dp[1]

        # if n>=2:
        #     dp[2] = min(dp[0]+costs[1]+4,dp[1]+costs[1]+1) 
        #     if n==2:
        #         return dp[2]

        # for j in range(3,n):
        #     opc1 = dp[j-3]+costs[j-1]+9
        #     opc2 = dp[j-2]+costs[j-1]+4
        #     opc3 = dp[j-1]+costs[j-1]+1
        #     dp[j] = min(opc1,opc2,opc3)
        
        # return dp[-1]


#maldito imbecil, nunca vas a servir para nada maldito fracasado!!!!!
#---------------------------------------------------------------------


        costs = [0]+costs

        dp = [float("inf")]*(n+1)

        dp[0] = 0
        
        
        for i in range(1,n+1):
            if i == 1:
                dp[i] = dp[i-1] + costs[i] + 1
            
            elif i == 2:
                dp[i] = min(dp[i-2]+costs[i]+4,dp[i-1]+costs[i]+1)

            else:
                dp[i] = min(dp[i-3]+costs[i]+9,dp[i-2]+costs[i]+4,dp[i-1]+costs[i]+1)
            
        return dp[-1]



