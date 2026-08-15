from functools import lru_cache

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        #sliding window no: A subsequence is an non-empty array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
        #dfs with memo, 2**n
        # propety  a(*)a' = 1



        # @lru_cache(maxsize=None)
        # def dfs(i,cnt,prev_num = None):
        #     if i == len(nums):
        #         if prev_num :
        #             return cnt
        #         return 0
            

        #     #tomando el curr_num
        #     if prev_num:
        #         opc1 =  dfs(i+1,cnt+1,prev_num ^ nums[i])
        #     else:
        #         opc1 =  dfs(i+1,cnt+1,nums[i])

        #     #no tomando:
        #     opc2 =  dfs(i+1,cnt,prev_num)
            
        #     return max(opc1,opc2)
        
        # return  dfs(0,0)



#eres un imbecil , Memory Limit Exceeded
#-------------------------------------------------        

        xor = 0
        zeros = 0

        for num in nums:
            xor ^= num
            if num == 0:
                zeros+=1
        
        if xor == 0:
            if zeros == len(nums):
                return 0
            return len(nums)-1
        return len(nums)
