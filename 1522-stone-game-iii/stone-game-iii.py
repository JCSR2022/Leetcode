class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        #brute force like you

        # size = len(stoneValue)

        # @cache
        # def dfs(i):
        #     if i >= size:
        #         return 0
            
        #     opc1 =  stoneValue[i] - dfs(i+1)
        #     opc2 = 0
        #     opc3 = 0    
        #     if i+1 < size:
        #         opc2 =  stoneValue[i]+stoneValue[i+1] - dfs(i+2)

        #     if i+2 < size:
        #         opc3 =  stoneValue[i]+stoneValue[i+1] +stoneValue[i+2] - dfs(i+3)

        #     return max(opc1,opc2,opc3)

        # ans = dfs(0) 
        # if ans > 0 :
        #     return "Alice"
        # elif ans == 0:
        #     return "Tie"
        # else:
        #     return "Bob"

# no funciona, por que maldota sea!!!!!!!!!!!!!!!!!!!1



        size = len(stoneValue)

        @cache
        def dfs(i):
            if i == size:
                return 0

            ans =float("-inf")
            for j in range(i,min(i+3,size)):
                ans = max(ans,sum(stoneValue[i:j+1])-dfs(j+1))
            
            return ans
           
        ans = dfs(0) 
        if ans > 0 :
            return "Alice"
        elif ans == 0:
            return "Tie"
        else:
            return "Bob"