class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def checkEating(n):
            hours = [math.ceil(bananas/n) for  bananas in piles]
            return sum(hours) <= h
        
        #binary search:
        l = 1 
        r = max(piles)
        ans = r
        while l<=r:
            m =l+(r-l)//2       #(l+r)//2 
            
            if checkEating(m):
                r = m-1
                ans = min(ans,m)
            else:
                l = m+1
        
        return ans