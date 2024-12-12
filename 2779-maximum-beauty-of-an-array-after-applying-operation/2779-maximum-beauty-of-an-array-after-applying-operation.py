class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        #aproach:
        # sort and slidign window size 2*k
        
#         if len(nums) == 1:
#             return 1
        
        
#         nums.sort()
#         max_dist = 2*k
        
#         max_count = 0
#         count = 0
#         L = 0
#         R = 0
#         while R < len(nums):
#             if nums[R] - nums[L] <  max_dist:
#                 count += 1
#                 max_count = max(max_count,count)
#             else:
#                 count -= 1
#                 L += 1
#             R +=1
            
            
#         return max_count
        
        
 #---------------------------------------------------------


        nums.sort()
        max_dist = 2*k
        ans = 0
        L = 0 
        
        for R in range(len(nums)):
            while nums[R] - nums[L] >  max_dist:
                L +=1
    
            ans = max(ans,R-L+1)
            
    
    
        return ans




        
        
        
        
        #------------------------------------------
        
#         # Extend the range for each element in nums
#         events = []
#         for num in nums:
#             events.append((num - k, 1))  # Start of range
#             events.append((num + k + 1, -1))  # End of range (exclusive)

#         # Sort events by value, and in case of tie, by type of event
#         events.sort()

#         # Use a sweep line approach to calculate the maximum overlap
#         max_beauty = 0
#         current_count = 0
#         for value, effect in events:
#             current_count += effect
#             max_beauty = max(max_beauty, current_count)

#         return max_beauty
        
#-----------------------------------------------------------------------


        
        