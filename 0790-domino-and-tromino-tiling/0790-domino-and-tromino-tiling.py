class Solution:
    def numTilings(self, n: int) -> int:

            # dp = defaultdict(int)
            # dp[(0,0)] = 0
            # min_n = 0

            # while min_n < n:
            #     new_dp = defaultdict(int)

            #     for (p1,p2),count in dp.items():
            #         if p1 == p2:
            #             #case #1: add one vertical domino
            #             new_dp[(p1+1,p2+1)] +=count+  1

            #             #case #2: add two horizontal domino
            #             new_dp[(p1+2,p2+2)] +=count+  1

            #             #case #3: add tromino (two on p2)
            #             new_dp[(p1+1,p2+2)] += count

            #             #case #4: add tromino (two on p1)
            #             new_dp[(p1+2,p2+1)] += count

            #         elif p1>p2:
            #             #case #5: add  horizontal domino on p2
            #             new_dp[(p1,p2+2)] += count

            #             #case #6: add  tromino on (two on p2)
            #             new_dp[(p1+1,p2+2)] += count +1   

            #         else:
            #             #case #7: add  horizontal domino on p1
            #             new_dp[(p1+2,p2)] += count  

            #             #case #6: add  tromino on (two on p1)
            #             new_dp[(p1+2,p2+1)] += count 

            #     min_n +=1
            #     # print(min_n)
            #     # print(dict(dp))
            #     # print(dict(new_dp))
            #     # print()
            #     dp = new_dp
                
            # return dp[(n,n)]

#no funciona
#---------------------------------------------------

        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2

        MOD = 10**9 + 7

        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        pre_sum = 1  # sum(dp[0] to dp[n-3])

        for i in range(3, n + 1):
            dp[i] = (dp[i-1] + dp[i-2] + 2 * pre_sum) % MOD
            pre_sum = (pre_sum + dp[i-2]) % MOD

        return dp[n]
















#-----------------------------------------------------
        # Aproach dinamic programing:
        # 2x1  = 1  [0]
        #           [0] 
        # 2x2  = 2       [0|0]    [0][0]
        #                [0|0]    [0][0]
        # 2x3  = 5
        # 2x4  = 6  


        #no tengo la mas puta idea
#---------------------------------------------------
        # #Ruslan Tsykaliak
        # #https://www.youtube.com/watch?time_continue=1&v=_0dSGJnYSA0&embeds_referring_euri=https%3A%2F%2Fleetcode.com%2F&source_ve_path=Mjg2NjY
        # #https://www.youtube.com/watch?v=CecjOo4Zo-g
        # MOD = 10**9 + 7
        # if n == 1: return 1  # Base case: only one way to tile a 2×1 board
        # if n == 2: return 2  # Base case: two ways to tile a 2×2 board
        # if n == 0: return 0  # Edge case: no board, no solution
        
        # # Initialize dp array with base cases
        # dp = [1, 1, 2]  # dp[0]=1 (empty), dp[1]=1, dp[2]=2
        
        # # Build up solutions iteratively
        # for i in range(3, n+1):
        #     # Formula: current solution = (solution from 3 steps ago + 2 * solution from 1 step ago) % MOD
        #     value = (dp[i-3] + 2 * dp[i-1]) % MOD
        #     dp.append(value)
        
        # return dp[-1]  # Return the solution for length n    

#-----------------------------------------------------------
















