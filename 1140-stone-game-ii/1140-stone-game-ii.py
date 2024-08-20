class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        
        
        

        #!#%@^#$^#%&$^&%^&%^ No work you pice of !@$@#!%@$##$^#$^ , 
        
        
        dp = {}
        
        # return max Alice
        def dfs(turn,i,M):
            
            if i >= len(piles):
                return 0
            
            if (turn,i,M) in dp:
                return dp[(turn,i,M)]
            
            ans = 0 if turn else float("inf")
            total = 0
            
            for X in range(1,M*2+1):
              
                if i + X > len(piles):
                    break
                
                total += piles[i+X-1]
                fut_val = dfs(not turn,i+X,max(M,X))
                
                ans = max(ans, total +fut_val) if turn else min(ans,fut_val)
            
            dp[(turn,i,M)] =ans
            
            return ans
                
        return dfs(True,0,1)        
                
    
    
    
    
    
    
    
#         # dp , one pointer:
    
#         dp = {}
#         # return max Alice
#         def dfs(turn,i,M):
#             print("turn,i,M,dp:",turn,i,M,dp)
            
#             if i >= len(piles):
#                 return 0
            
#             #cashing
#             if (i,M) in dp:
#                 return dp[(i,M)]
                
#             posibles = []
#             for X in range(1,M*2+1):
#                 print("posibles:",posibles)
#                 if i+X <=  len(piles):
#                     new_m = max(M,X)

#                     val = sum(piles[i:i+X]) if turn else 0

#                     fut_val = dfs(not turn,i+X,new_m)
                
#                     posibles.append( val + fut_val )
            
            
#             dp[(i,M)] = max(posibles)
            
#             return dp[(i,M)]
                
#         return dfs(True,0,1)        
                
                
            
            
            