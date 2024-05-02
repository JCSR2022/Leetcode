class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #Binary search
        
#         l = 0
#         r = len(nums)-1
        
#         while l+1 < r:
    
#             m =  l +(r-l)//2     #(l+r)//2  
#             print(l,m,r)
#             #print((l,nums[l]),(m,nums[m]),(r,nums[r]))

#             if nums[m] == target:
#                 return m
#             if nums[l] == target:
#                 return l
#             if nums[r] == target:
#                 return r
            
            
#                 #print(f"found,{target} in index {m}")
#                 #break

#             if nums[m] < nums[l]:
#                 if nums[r] < target:
#                     r = m
#                 else:
#                     l = m
#             else: 
#                 if nums[m] > target:
#                     r = m
#                 else:
#                     l = m
#         return -1



        l , r  = 0 , len(nums) -1
    
        while l <= r:
            m =  l +(r-l)//2    
            
            if target == nums[m]:
                return m
            
            #left
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            
            #right
            else:
                if target < nums[m] or target>nums[r]:
                    r = m - 1
                else: 
                    l = m + 1
                    
                    
        return -1