class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        #brute force
        # ans = 0
        # N = len(nums)

        # for i in range(N):
        #     for j in range(i,N):
                
        #         max_ele = max(nums[i:j+1])
        #         min_ele = min(nums[i:j+1])
        #         if max_ele + min_ele <=target:
        #             ans +=1
        #         print(nums[i:j+1],max_ele,min_ele,ans)
        # return ans
        #Nooooo
 #---------------------------------------------        
        #brute force
        # ans = 0
        # N = len(nums)

        # for i in range(1,2**N):
        #     mask = bin(i)[2:].zfill(N)
        #     curr = [n for n,mask in zip(nums,mask) if mask == "1" ]
        #     if max(curr)+min(curr) <= target:
        #         ans+=1
        #         print(i,curr)

        # return ans
#of curse Time Limit Exceeded
#----------------------------------------------------------------------
        #aproach 2

        # nums.sort()
        # ans = 0
        # MOD = 10**9 + 7 

        # for i,x in enumerate(nums):
        #     n = bisect.bisect_right(nums,target-x)-1
        #     if n - i - 1 >=0:
        #         ans += pow(2,n -1, MOD) -1
        #     if x * 2 <= target:
        #         ans += 1
        #     ans %= MOD

        # return ans % MOD 

#hoy no
#---------------------------------------
        """
        Sort array to control min/max
        Use left/right pointers to find valid pairs
        Each valid pair contributes 2^(window size) subsequences
        Sum counts and return modulo result
        """
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)

        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % mod

        left, right = 0, n - 1
        result = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                result = (result + power[right - left]) % mod
                left += 1
            else:
                right -= 1

        return result




