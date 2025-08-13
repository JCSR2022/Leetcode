class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        
        Mod = 10**9+7

        #brute force try all posible combinations
        myMemory = {}
        def dfs(curr_sum,curr_nk):
            if curr_sum == n:
                return 1

            if curr_sum > n or  curr_nk**x > n:
                return 0

            if (curr_sum,curr_nk) in myMemory:
                return myMemory[(curr_sum,curr_nk)]

            #try this 
            op1 = dfs(curr_sum+curr_nk**x,curr_nk+1)%Mod

            #skip 
            op2 = dfs(curr_sum,curr_nk+1)%Mod


            myMemory[(curr_sum,curr_nk)] = (op1 + op2)%Mod
            return myMemory[(curr_sum,curr_nk)]

        return dfs(0,1)

#Time Limit Exceeded
#-------------------------------------------