class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        # #brute force: n^2
        # ans = 0
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         #print(i,j,(nums[i],nums[j]))
        #         n = nums[i]+nums[j]
        #         if lower <= n and n <= upper: ans +=1  
        # return ans
        
        #---------------------------------------------------
        
        # using binary search n*log(n)
        
#         def binarysearch_lower(num,arr):
#             # will return position on arr of elements > lower-num
#             search = lower-nums
#             l = 0
#             r = len(arr)
#             m = r-l
            
#             while l<r:
#                 if arr[m] >= search
                
                
                
#             return m
            
            
            
            
#         def binarysearch_upper(num,arr):
#             # will return position on arr of elements < upper-num
            
            
            
#         nums.sort()
#         ans = 0
        
#         for i,n in enumerate(nums):
#             left_p = binarysearch_lower(num,nums[i+1:])
#             right_p = binarysearch_upper(num,nums[i+1:])
#             ans += right_p - left_p
            
#         return ans
        
#------------------------------------------------------------------


        def bin_search(l,r,target):
            #return largest i, where nums[i]< target
            
            while l <= r:
                m = l +(r-l)//2
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            return r
        
        
        nums.sort()
        ans = 0
        
        
        for i in range(len(nums)):
            low = lower - nums[i]
            up  = upper - nums[i]
            
            right_p = bin_search(i+1,len(nums)-1,up +1)
            left_p  = bin_search(i+1,len(nums)-1,low)
            
            ans += right_p-left_p
        
        
        return ans
        