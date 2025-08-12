class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        #brute force to check if understand problem..
        Mod = 10**9+7

        # power = [ 2**i for i,j in enumerate(bin(n)[2:][::-1]) if j =='1' ]
       
        # pre = [power[0]]
        # ans = []
        # for i,j in queries:
        #     ans.append(math.prod(power[i:j+1])%Mod)

        # return ans
        
        #---------------------------------------------------------------

        power = [ 2**i for i,j in enumerate(bin(n)[2:][::-1]) if j =='1' ]
        print(power)

        pre = [power[0]]
        for i in range(1,len(power)):
            pre.append( pre[-1]*power[i])
        print(pre)
        
        ans = []
        for i,j in queries:
            if i == 0:
                ans.append(pre[j]%Mod)
            else:
                ans.append( (pre[j]//pre[i-1])%Mod)

        return ans
        