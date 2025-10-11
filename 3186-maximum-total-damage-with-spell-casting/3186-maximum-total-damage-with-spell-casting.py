class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:


        #para reveisar mañana!!!
        #https://www.youtube.com/watch?v=SDx3YSCr9ck



        freq = Counter(power)
        keys = sorted(freq)
        n = len(keys)
        dp = [0] * n
        dp[0] = freq[keys[0]] * keys[0]
        for i in range(1, n):
            take = freq[keys[i]] * keys[i]
            l, r, ans = 0, i - 1, -1
            while l <= r:
                mid = (l + r) // 2
                if keys[mid] <= keys[i] - 3:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            if ans >= 0:
                take += dp[ans]
            dp[i] = max(dp[i - 1], take)
        return dp[-1]




        # #make dict max_power with sum of each power[i]..

        # max_power =  [0] *( max(power) + 1) 
        # for p in power:
        #      max_power[p] += p

        # print(max_power)

        # ans = []
        # curr_max = 0
        # for i in range(2,len(max_power)-2 ):
        #    curr_max = max(max_power[i-2],max_power[i-1] ,max_power[i],max_power[i+1],max_power[i+2]  ) 
        #    ans.append(curr_max) 

        # print(ans)

        # return 13+13+16+12+5
        








        