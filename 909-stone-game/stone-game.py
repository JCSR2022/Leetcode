class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        #brut force again

        @cache
        def dfs(i,j):
            if i == j:
                return piles[i]
            
            opc1 = piles[i] - dfs(i+1,j)
            opc2 = piles[j] - dfs(i,j-1)

            return max(opc1,opc2)

        return dfs(0,len(piles)-1)  > 0 

