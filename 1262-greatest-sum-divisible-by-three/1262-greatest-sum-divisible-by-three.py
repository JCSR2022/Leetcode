class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        """
        using dp of 3 posibilities n%3 = [0,1,2]
        
        nums = [3,6,5,1,8]


        dp = {0:0, 1:0, 2:0}    3+0=3%3->0,     3+0=3%3->0,     3+0=3%3->0          new_dp = {0:3, 1:0, 2:0}
        dp = {0:3, 1:0, 2:0}    6+3=9%3->0,     6+0=6%3->0,     6+0=6%3->0          new_dp = {0:9, 1:0, 2:0}
        dp = {0:9, 1:0, 2:0}    5+9=14%3->2,    5+0=5%3->2,     5+0=5%3->2          new_dp = {0:9, 1:0, 2:14}
        dp = {0:9, 1:0, 2:14}   1+9=10%3->1,    1+0=1%3->1,     1+14=15%3->0        new_dp = {0:15,1:10,2:14}
        dp = {0:15,1:10,2:14}   8+15=23%3->2    8+10=18%3=>0    8+14=22%3->1        new_dp = {0:18,1:22,2:23}


        """


        # dp = {0:0,1:0,2:0}
        # for n in nums:
        #     new_dp = {0:0,1:0,2:0}
        #     for res,max_sum in dp.items():
        #         new = n + max_sum
        #         print(res,max_sum,"...",new,new_dp[new%3])
        #         new_dp[new%3] = max(dp[new%3],new)  
                
        #     print(dp, new_dp)
        #     dp = { res:max(cur_sum,new_dp[res] ) for res,cur_sum in dp.items() }

        # return dp[0]

#---------------------------------------------------------------
#Maldita basura que no puedes hacer una mierda!!!!!!
#@#%@^%$&%^&*$*$^*%^*^&*&^%&*%^*^%

        # size = len(nums)

        # dp = [ [0]*3 for _ in range(size)]

        # dp[0][nums[0]%3]=nums[0]

        # for i in range(1,size):
        #     for j in range(3):
        #         new = dp[i-1][j] + nums[i]
                
        #         dp[i][new%3] = max(dp[i-1][new%3],new)

        #no, no se hacerlo

#-------------------------------------------------         

        # f = [0,float("-inf"),float("-inf")]

        # for num in nums :
        #     g = f[:]
        #     rem = num % 3
        #     for r in range(3):
        #         old_sum = f[r]
        #         if old_sum == float("-inf"):
        #             continue
        #         new_r =(r + rem)%3
        #         new_sum = old_sum + num
        #         g[new_r]=max(g[new_r],new_sum)
        #     f = g
        # return f[0] 
        

#Esta era la otra forma,         
        a = [x for x in nums if x % 3 == 0]
        b = sorted([x for x in nums if x % 3 == 1], reverse=True)
        c = sorted([x for x in nums if x % 3 == 2], reverse=True)

        ans = 0
        lb, lc = len(b), len(c)
        for cntb in [lb - 2, lb - 1, lb]:
            if cntb >= 0:
                for cntc in [lc - 2, lc - 1, lc]:
                    if cntc >= 0 and (cntb - cntc) % 3 == 0:
                        ans = max(ans, sum(b[:cntb]) + sum(c[:cntc]))
        return ans + sum(a)
        