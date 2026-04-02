class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:

        #aproach dp wirh row fill with: 
        #[total, arr_with_3_min_robberies[] ]


        # m = len(coins)
        # n = len(coins[0])
        # dp_row = [  [0,[]] for _ in range(n) ]

        # for i in range(m):
        #     curr_row  = [ [0,[]] for _ in range(n) ]
        #     for j in range(n):
        #         left = curr_row[j-1] if j>0 else [0,[]]
        #         up = dp_row[j] 
        #         curr_row[j][0] = max(left[0],up[0]) + coins[i][j]

        #         if coins[i][j]<0:
                    
                    
        #         else:
        #             curr_row[j][1] = dp_row[j][1]
#maldito imbecil!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
#-------------------------------------------------------

        m, n = len(coins), len(coins[0])
        dp = [[-inf] * 3 for _ in range(n+1)]
        dp[0][0] = 0
        for row in coins:
            for i, coin in enumerate(row):
                for k in range(3):
                    dp[i][k] = max(dp[i][k], dp[i-1][k]) + coin
                if coin < 0:
                    dp[i][1:] = max(dp[i][1], dp[i][0] - coin), max(dp[i][2], dp[i][1] - coin)
        return max(dp[-2])

                



        