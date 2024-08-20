from collections import deque

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        #JAJAJAJAJA
        #because even number of piles
        # alice can always choose all even num or all odds
        # and always one of the summ, all odd or all even is going to be grater 
        
        # return True
        
        
        
        # sol using cashing on dp an two painters O(n**2)
        
        dp = {}
        
        # return max of alice choices.
        def dfs(l,r):
            if l>r:
                return 0
            
            #cashing so no work is repited:
            if (l,r) in dp:
                return dp[(l,r)]
            
            #confirm is alice choice:
            alice = True if (r-l)%2 == 0 else False
            
            left = piles[l] if alice else 0
            right = piles[r] if alice else 0
            
            dp[(l,r)] =   max(dfs(l+1,r)+left,dfs(l,r-1)+right)          
            
            return dp[(l,r)]
            
        max_alice = dfs(0,len(piles)-1)
        
        return max_alice > sum(piles)//2
        
        
        
        
        
        
        
        
        
        