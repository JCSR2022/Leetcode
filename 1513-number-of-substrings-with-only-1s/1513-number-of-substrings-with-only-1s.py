class Solution:
    def numSub(self, s: str) -> int:

        MOD = 10**9+7

        #sliding window?
        s_num = [int(ch) for ch in s] 

        ans = 0
        size = 0
        for i in range(len(s_num)):
            if s_num[i] == 1:
                size += 1
            else:
                ans += size*(size+1)//2
                ans %= MOD
                size = 0
                
        ans += size*(size+1)//2
        ans %= MOD
        return ans
            

        