class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

#         # brute force aproach: 
        
#         maxSubarray = 0
#         n = len(nums)
#         for i in range(n):
#             for j in range(i, n):
#                 if nums[i:j+1].count(1) == nums[i:j+1].count(0):
#                     maxSubarray = max(maxSubarray,len(nums[i:j+1]))

#         return maxSubarray 
    
    
    
        #Sliding Window NOT WORK

        
        # https://www.youtube.com/watch?v=agB1LyObUNE
        # neet code solution
        
        zero, one = 0,0
        res = 0
        diff_index = {}


        for i,n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one +=1

            if one-zero not in diff_index:
                diff_index[one-zero] = i

            if one == zero:
                res = one + zero
            else:
                idx = diff_index[one-zero]
                res = max(res,i-idx)
        return res
        
        
        
        
        
        
        