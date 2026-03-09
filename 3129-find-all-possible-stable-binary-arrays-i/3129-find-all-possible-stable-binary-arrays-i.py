class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:

        #vayanse a la mierda

        mod = 10 ** 9 + 7

        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]  # i 0s + j 1s ending with 0
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]  # i 0s + j 1s ending with 1

        # Base cases: only zeros or only ones => only one string if len <= min(limit, zero/one)
        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1

        # DP iterations
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                dp0[i][j] = sum(dp1[i - k][j] for k in range(1, min(limit, i) + 1)) % mod
                dp1[i][j] = sum(dp0[i][j - k] for k in range(1, min(limit, j) + 1)) % mod

        return (dp0[zero][one] + dp1[zero][one]) % mod



#i will try to brute force, dfs aproach with memorization to see if work


        # def dfs(cnt_zeros,cnt_ones,sub_arr):
            
        #     if cnt_zeros == zero and cnt_ones == one:
        #         return 1

        #     opc0 = 0
        #     opc1 = 0
        #     if cnt_zeros < zero:
        #         new_sub = sub_arr+"0"
        #         if len(new_sub)>limit:
        #             last_ceros = new_sub[-limit-1:].count('1')
        #             last_ones  = new_sub[-limit-1:].count('0')
        #             if last_ceros > 0 and last_ones > 0:
        #                 opc0 = dfs(cnt_zeros+1,cnt_ones,new_sub)                

        #     if cnt_ones < one:  
        #         new_sub = sub_arr+"1"
        #         if len(new_sub)>limit:
        #             last_ceros = new_sub[-limit-1:].count('1')
        #             last_ones  = new_sub[-limit-1:].count('0')
        #             if last_ceros > 0 and last_ones > 0:
        #                 opc1 = dfs(cnt_zeros,cnt_ones+1,new_sub)
            
        #     return opc0 + opc1

        # return dfs(0,0,'')
#Que sorpresa, no funciona , pendejo!!!
#Today I can do it, i guess is somthing like dp 
