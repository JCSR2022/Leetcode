class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        #brute force n**2
        
#         maxWidth = 0
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if j > i and nums[j]>=nums[i]:
#                     maxWidth = max(maxWidth, j-i)
#         return maxWidth 

        #teo pointers prefix sol
    
        max_n = float("-inf") 
        max_nums = []
        for n in nums[::-1]:
            max_n = max(max_n,n)
            max_nums.append(max_n)
        max_nums = max_nums[::-1]
        
        
        res  = 0
        l = 0

        for r in range(len(nums)):
            while nums[l] > max_nums[r]:
                l += 1
            res  = max(res,r-l)
            
        return res

        