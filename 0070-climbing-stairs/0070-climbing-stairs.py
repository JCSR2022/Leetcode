class Solution:
    def climbStairs(self, n: int) -> int:
        # Best explain: https://www.youtube.com/watch?v=Y0lT9Fck7qI
        
        # one = 1
        # two = 1
        
        #for i in range(n-1):
        #    two,one = one, one+two   
        #return one
        
        #Esto esta mal, esto no puede ser mas rapido que la solucion anterior
        dp = [1,1]
        for i in range(n-1):
            dp.append(dp[i]+dp[i+1])
        return dp[-1]
