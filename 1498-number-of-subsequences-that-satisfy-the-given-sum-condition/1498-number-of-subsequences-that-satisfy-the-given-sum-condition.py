class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        MOD = 10**9+7
        N = len(nums)
        nums.sort()

        l = 0
        r = N-1
        ans = 0
        while l<=r:
            if nums[l]+nums[r] <= target:
                size = r-l
                ans = (ans + pow(2,size,MOD))%MOD
                l +=1
            else:
                r -=1
        
        return ans


#----------------------------------------------------------------------
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
#of course Time Limit Exceeded
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
        # mod = 10**9 + 7
        # nums.sort()
        # #print(nums)

        # n = len(nums)
        
        # powers = {}
        # def power(i):
        #     if i in powers:
        #         return powers[i]
        #     powers[i] = pow(2, i, mod)
        #     return powers[i]
        # # @lru_cache(maxsize=None)
        # # def power(i):
        # #     return pow(2, i, mod)

        # left, right = 0, n - 1
        # result = 0
        # while left <= right:
        #     #print(nums[left:right+1], power(right - left) if nums[left] + nums[right] <= target else "no valid",result)
        #     if nums[left] + nums[right] <= target:
        #         result = (result + power(right - left)) % mod

        #         # #if want to visualize ans-----------
        #         # print(nums[left:right+1], power(right - left))
        #         # curr_n = right - left 
        #         # cur_ans = [] 
        #         # if curr_n > 1:
        #         #     for i in range(2**curr_n):
        #         #         mask = bin(i)[2:].zfill(curr_n)
        #         #         curr = [x for x,mask in zip(nums[left+1:right+1],mask) if mask == "1" ]
        #         #         cur_ans.append([nums[left]]+curr)
        #         #     cur_ans.sort(key=lambda x: (len(x), x))
        #         #     print(cur_ans)
        #         # else:
        #         #     print([nums[left]])
        #         # #-----------------------------------

        #         left += 1
        #     else:
        #         right -= 1

        # return result




