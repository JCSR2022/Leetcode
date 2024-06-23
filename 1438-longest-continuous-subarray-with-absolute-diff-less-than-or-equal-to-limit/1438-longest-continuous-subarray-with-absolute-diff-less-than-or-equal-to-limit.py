class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        
        #No lo pude hacer funcionar porque la logica esta mal, necesito usar
        # una cola para almacenar los maximos y minimos, cuando se mueve
        # el puntero izquierdo necesito encontrar el maximo y minimo remanente 
        # en la ventana
        
        # Monoctonic queue 
        #https://www.youtube.com/watch?v=V-ecDfY5xEw
        
        min_q = deque() #monotonic increasing
        max_q = deque() #monotonic decreasing
        
        l = 0
        res = 0
        
        for r in range(len(nums)):
        
            while min_q and nums[r] < min_q[-1]:
                min_q.pop()
                
            while max_q and nums[r] > max_q[-1]:
                max_q.pop()
                
            min_q.append(nums[r])
            max_q.append(nums[r])
            
            while max_q[0] - min_q[0] > limit:
                if nums[l] == max_q[0]:
                    max_q.popleft()
                if nums[l] == min_q[0]:
                    min_q.popleft()
                l += 1
            
            
            res = max(res,r - l + 1)
        
        
        return res
        
        
        
        
        
        
        
#        
#         increase = deque()
#         decrease = deque()
#         max_length = 0
#         left = 0

#         for right in range(len(nums)):
#             while increase and nums[right] < increase[-1]:
#                 increase.pop()
#             increase.append(nums[right])
            
#             while decrease and nums[right] > decrease[-1]:
#                 decrease.pop()
#             decrease.append(nums[right])
            
#             while decrease[0] - increase[0] > limit:
#                 if nums[left] == increase[0]:
#                     increase.popleft()
#                 if nums[left] == decrease[0]:
#                     decrease.popleft()
#                 left += 1
                
#             max_length = max(max_length, right - left + 1)
        
#         return max_length
        
        
        
        
        
        
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
            
