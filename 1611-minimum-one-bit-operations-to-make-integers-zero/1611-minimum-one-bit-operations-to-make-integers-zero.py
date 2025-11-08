class Solution:
    def minimumOneBitOperations(self, n: int) -> int:


        #dp[]
        #recursion to build dp
        # if next = 1 and remainig  

        #n = 4,  100
        #1. op1 101  
        #2. op2 111
        #3. op1 110
        #4. op2 010   ->n=2  
        #5. op1 011   ->n=3  ret 2
        #6. op2 001   ->n=1  ret 1  
        #7. op1 000   ->n=0  ret 0


        # n=8, 1000
        #1. op1     1001   n = 9   to covert i=3 ->1 need i =2 ->1 ...
        #2. op2 i=1 1010   n = 10
        #3. op2 i=2 1110   n = 14
        #4. op1     1111   n = 15
        #5. op2 i=1 1101   n = 13
        #6  op1     1100   n = 12
        #7  op2 i=3 0100   n = 4
        #+7 n=4
        

        #   0  -> ret 0
        #   1  -> ret 1
        #  10  -> covert_to_one(i=0) + 1 + ret(i=0)
        #  11  -> 1+ ret(i=0)
        # 100  -> covert_to_one(i=1) + 1 +ret(i=1)

        #  100000 -> convert_to_one(0,i=4) + 1 + ret(i=4) 


        #  dp     
        #  change/digit| 0 | 1 | 2 |      i      |
        #--------------------------------------------- 
        #       cnt    | 1 | 3 | 7 | 2*dp[i-1]+1 |
        #---------------------------------------------

        #n => 10**9 can have as 
        #print(bin(10**9+1)[2:],len(bin(10**9+1)[2:]))

        # max_bin_dig = len(bin(10**9+1)[2:]) 
        
        # dp = [0]*(max_bin_dig+1)
        # dp[0] = 1
        # for i in range(1,max_bin_dig+1):
        #     dp[i] = dp[i-1]*2+1
    
        # ans = 0
        # digits = [ int(x) for x in bin(n)[2:] ]
        # print(bin(n)[2:],list(reversed(digits)))    
        
        # for i,d in enumerate(reversed(digits)):
        #     if d:
        #         ans += dp[i]
        #     print(i,d,dp[i],ans)
        # return ans

#noooo, toda la logica esta mal!!!!!!
#--------------------------------------------------------
        def f(n):
            if n<=1: return n
            k=int(log2(n))
            return (1<<(k+1))-1-f(n^(1<<k))
        return f(n)