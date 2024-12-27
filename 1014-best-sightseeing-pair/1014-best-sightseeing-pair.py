class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        #brute force
        #try all, n**2
        
#         ans = 0
#         for i in range(len(values)-1):
#             for j in range(i+1, len(values)):
#                 ans = max(ans,values[i] + values[j] + i - j)
#                 #print(i,j,values[i],values[j],values[i] + values[j] + i - j,ans)
        
#         return ans

#Time Limit Exceeded
#---------------------------------------------------------------

# 2 pointers aproach

        L = 0 
        ans = float("-inf")
        for R in range(1,len(values)):
            ans = max(ans,values[L]+values[R]+L-R)
            if values[R] > values[L]+L-R:
                L = R
            
        return ans
            
        

        
        