class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
#         pos = []
#         neg = []
#         for num in nums:
#             if num >= 0:
#                 pos.append(num)
#             else:
#                 neg.append(num)
        
#         ans = [ pos.pop(0) if i%2 ==0 else  neg.pop(0) for i in range(len(nums))]
        
#         return ans

        limit = len(nums)-1
        ans = []

        p = 0  # positive pointer 
        n = 0  # Negative pointer
        while len(ans) < len(nums) :
            # print((p,nums[p]),(n,nums[n]))
            while nums[p] < 0:
                p += 1
            ans.append(nums[p])
            p += 1
            while nums[n] >= 0:
                n += 1
            ans.append(nums[n])
            n += 1
        return ans    
                
        