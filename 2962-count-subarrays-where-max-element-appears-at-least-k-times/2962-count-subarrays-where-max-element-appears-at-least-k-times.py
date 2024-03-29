class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        # # brute force:
        # countSub = 0
        # maxElem = max(nums)
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         if nums[i:j+1].count(maxElem) >= k: countSub +=1
        #         print(i,j,nums[i:j+1],nums[i:j+1].count(maxElem) >= k,countSub)   
        # return countSub
        
        
        
        
        # aproach:
        # sliding window:
        # first find maxElem = max(nums)
        # create: 
        #    2 pointers: l=0, r=1 , 
        #    countApMax = 0 if nums[0] != maxElem 
        #    countSub = 0  
        # 1. while r < len(nums)
        #    if nums[l:r].count(maxElem) >= k:
        #         countSub += len(nums[r:])
        #          l +=1 , r = l+1
        #    r+=1
        
#         countSub = 0
#         maxElem = max(nums)
#         l = 0
#         r = 1
#         while l < len(nums)-1:
#             print(l,r,nums[l:r],nums[l:r].count(maxElem) >= k,countSub)
#             if nums[l:r].count(maxElem) >= k:
#                 countSub += len(nums)-r+1
#                 l += 1
#                 r = l
#             if r < len(nums):
#                 r += 1
        
#         return countSub

        max_n = max(nums)
        max_cnt = 0
        l = 0
        ans = 0
        
        for r in range(len(nums)):
            if nums[r] == max_n:
                max_cnt += 1
                
            while (max_cnt > k) or (l <= r and max_cnt == k and nums[l] != max_n):
                if nums[l] == max_n:
                    max_cnt -=1
                l +=1 
            if max_cnt == k:
                ans += l + 1
        return ans






        
        
        
        
        