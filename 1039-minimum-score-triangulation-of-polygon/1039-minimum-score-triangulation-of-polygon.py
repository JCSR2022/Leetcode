class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        #using dynamic Programming
        #https://www.youtube.com/watch?v=zvz0lETGO9w

        #i,j,k will be index of vertices over arr values

        @cache
        def dp(i,j):
            
            #it is not possible to do a triangle
            if j - i < 2 :
                return 0

            ans = float("inf")
            for k in range(i+1,j):
                curr = values[i] * values[j]* values[k]
                ans = min(ans, curr + dp(i,k) + dp(k,j) )

            return ans

        return dp(0,len(values)-1)


        