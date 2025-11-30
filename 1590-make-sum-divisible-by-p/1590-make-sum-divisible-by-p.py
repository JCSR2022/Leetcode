class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        #https://www.youtube.com/watch?v=7FJrMTpadRI

        total =sum(nums)
        remain = total % p

        if remain == 0 :
            return 0

        res = len(nums)
        cur_sum = 0
        remain_to_idx = {0:-1}

        for i,n in enumerate(nums):
            cur_sum = (cur_sum + n)%p
            prefix = (cur_sum - remain + p) % p
            if prefix in remain_to_idx:
                cur_len = i - remain_to_idx[prefix]
                res = min(res,cur_len)
            remain_to_idx[cur_sum] = i

        return -1 if res == len(nums) else res





#--------------------------------------------------------------------
#no funciona, como tu 

        # size = len(nums)
        # target = sum(nums)%p

        # if target == 0:
        #     return 0

        # prefix = [0]*size
        # prefix[0] = nums[0]
        # for i in range(1,size):
        #     prefix[i] = nums[i]+prefix[i-1]
        
        # print(prefix)
        
        # min_len = float("inf")
        # for l in range(size):
        #     for r in range(l+1,size):
        #         print((l,r),prefix[r]-prefix[l],(prefix[r]-prefix[l])%p)
        #         if (prefix[r]-prefix[l])%p == target:
        #             min_len = min(min_len,r-l)

     

        # return min_len if min_len < float("inf") else -1















        #------------------------------------------------------------------------------
        
        #brute force
        # calculate sum(arr)
        # try removing 1 elem and check if (sum(arr)-arr[i])%p==0
        # try removing n elem and check if (sum(arr)-arr[i:i+n])%p==0
        
#         suma = sum(nums)
#         if suma%p == 0:
#             return 0
        
#         for n in range(1,len(nums)):
#             for i in range(len(nums)):
#                #print(n,i,nums[i:i+n])#,suma-nums[i:i+n],(suma-nums[i:i+n])%p == 0)
#                 if (suma-sum(nums[i:i+n]))%p == 0 :
#                     return n
                
#         return -1

#------------------------------------------------------------------------------------------------
        # #today not even try , tK Swap24
        # rem = sum(nums) % p
        # if rem == 0:
        #     return 0
        # length = len(nums)
        # h = {0: -1}    # dictionary where 
        #                # 1. key = remainder of running sum at each index, and
        #                # 2. value = index
        # run = [0]    # array to keep track of running sum
        # for i, num in enumerate(nums):
        #     run.append(run[-1] + num)
        #     curr = run[-1] % p
        #     if curr >= rem:
        #         if curr - rem in h:    # this portion of the array nums contributes to 'rem'; i.e. gross remainder
        #             length = min(length, i - h[curr - rem])
        #     else:
        #         if p - rem + curr in h:    # again, this portion contributes to 'rem'
        #             length = min(length, i - h[p - rem + curr])
        #     h[curr] = i    # update every time to keep track of the latest occurrence of a particular remainder
        # if length == len(nums):
        #     return -1
        # return length