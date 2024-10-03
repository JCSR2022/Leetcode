class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        
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



        rem = sum(nums) % p
        if rem == 0:
            return 0
        length = len(nums)
        h = {0: -1}    # dictionary where 
                       # 1. key = remainder of running sum at each index, and
                       # 2. value = index
        run = [0]    # array to keep track of running sum
        for i, num in enumerate(nums):
            run.append(run[-1] + num)
            curr = run[-1] % p
            if curr >= rem:
                if curr - rem in h:    # this portion of the array nums contributes to 'rem'; i.e. gross remainder
                    length = min(length, i - h[curr - rem])
            else:
                if p - rem + curr in h:    # again, this portion contributes to 'rem'
                    length = min(length, i - h[p - rem + curr])
            h[curr] = i    # update every time to keep track of the latest occurrence of a particular remainder
        if length == len(nums):
            return -1
        return length