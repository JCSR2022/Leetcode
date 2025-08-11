class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        #brute force to check if understand problem..


        power = [ 2**i for i,j in enumerate(bin(n)[2:][::-1]) if j =='1' ]
       
        ans = []
        for i,j in queries:
            ans.append(math.prod(power[i:j+1]))

        return ans
        
        