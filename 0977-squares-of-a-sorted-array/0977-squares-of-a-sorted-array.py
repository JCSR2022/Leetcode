class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #Two pointers sol
        
        
        
        n = len(nums)
        res = [0] * n
        L,R = 0 , n-1
        
        for i in range(n-1,-1,-1):
            if abs(nums[L])>abs(nums[R]):
                val = nums[L]
                L += 1
            else:
                val = nums[R]
                R -=1
            res[i] = val**2
        
        return res

        
#         r = len(nums)-1
#         l = 0
#         v_l = nums[l]**2
#         v_r = nums[r]**2
        
#         ans = [0]*len(nums)
#         i=0
#         while l <= r:
           
#             if v_r > v_l:
#                 ans[i] = v_r
#                 i+=1
#                 if r > 0:
#                     r -= 1
#                     v_r = nums[r]**2
#                 else:
#                     l += 1
#                     v_l = nums[l]**2
#             else:
#                 ans[i] = v_l
#                 i += 1
#                 if l < len(nums)-1:
#                     l +=1
#                     v_l = nums[l]**2
#                 else:
#                     r -=1
#                     v_r = nums[r]**2
                    
#         return ans[::-1]

                
                
            
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
                
                
        
        
        