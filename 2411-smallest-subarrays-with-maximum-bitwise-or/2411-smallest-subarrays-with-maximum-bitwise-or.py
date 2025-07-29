class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        #sliding window???
        # first find maxBitBiseoOr
        # nums[i] <= 10**9 
        # can be express as dict of bits?
        #need maxBitBiseoOr ending at x

        #brute force O(n**2)
        # n = len(nums)
        # maxBitWiseOr = [0]*n
        # maxBitWiseOr[-1] = nums[-1]
        # for i in range(n-2,-1,-1):
        #     maxBitWiseOr[i] = nums[i] | maxBitWiseOr[i+1]
      
        # ans = [0]*n
        # for i in range(n):
        #     curr_BitWiseOr = nums[i]
        #     size = 0
        #     for j in range(i,n):
        #         size += 1
        #         curr_BitWiseOr |= nums[j]
        #         if curr_BitWiseOr == maxBitWiseOr[i]:
        #             ans[i]= size
        #             break 
        
        # return ans
#Time Limit Exceeded
#---------------------------------
#$@#^#$^#$^#$&^%$&$^&%^^*R^*^**%$&

        last = [-1] * 32
        for i in range(len(nums) - 1, -1, -1):
            for b in range(32):
                if nums[i] & (1 << b):
                    last[b] = i
            nums[i] = max(1, max(last) - i + 1)
        return nums





        
        

        

        