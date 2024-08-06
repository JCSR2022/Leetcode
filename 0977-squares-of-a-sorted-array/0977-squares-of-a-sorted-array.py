class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #Two pointers sol
        
        r = len(nums)-1
        l = 0
        
        ans = []
        while l <= r:
            v_l = nums[l]**2
            v_r = nums[r]**2
    
            if v_r > v_l:
                ans.append(v_r)
                if r > 0:
                    r -= 1
                else:
                    l += 1
            else:
                ans.append(v_l)
                if l < len(nums)-1:
                    l +=1
                else:
                    r -=1
                    
        return ans[::-1]

                
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         left = 0
#         right =len(nums)-1
#         ans = []
        
#         while left<= right:
#             if abs(nums[left])>abs(nums[right]):
#                 ans.append(nums[left]**2)
#                 left +=1
#             else:
#                 ans.append(nums[right]**2)
#                 right -=1
            
            
#         return ans[::-1]
                
                
        
        
        