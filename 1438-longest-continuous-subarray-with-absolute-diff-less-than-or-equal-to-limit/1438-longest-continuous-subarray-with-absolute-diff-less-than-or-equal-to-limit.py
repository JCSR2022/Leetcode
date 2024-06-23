class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        increase = deque()
        decrease = deque()
        max_length = 0
        left = 0

        for right in range(len(nums)):
            while increase and nums[right] < increase[-1]:
                increase.pop()
            increase.append(nums[right])
            
            while decrease and nums[right] > decrease[-1]:
                decrease.pop()
            decrease.append(nums[right])
            
            while decrease[0] - increase[0] > limit:
                if nums[left] == increase[0]:
                    increase.popleft()
                if nums[left] == decrease[0]:
                    decrease.popleft()
                left += 1
                
            max_length = max(max_length, right - left + 1)
        
        return max_length
        
        
        
        
        
        
#         #two pointers, and to var max and min:
#         #NO LO PUDE HACER FUNCIONAR #%$#$^%#$^#$^^&%^
#         l = 0
#         min_val = float('inf')
#         max_val = float('-inf')
#         diff = 0
#         ans = 0
        
#         for r in range(len(nums)):
#             print(1,(l,nums[l]),(r,nums[r]),min_val,max_val,diff,ans)
            
#             min_val = min(min_val,nums[r])
#             max_val = max(max_val,nums[r])
#             diff = max_val-min_val
            
#             if diff > limit:
#                 l = r
#                 min_val = float('inf')
#                 max_val = float('-inf')
#             else:    
#                 ans = max(ans,r-l+1)
#             print(2,(l,nums[l]),(r,nums[r]),min_val,max_val,diff,ans)
            
#         return ans
            
