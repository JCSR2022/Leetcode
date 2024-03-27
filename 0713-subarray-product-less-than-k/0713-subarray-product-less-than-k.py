class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # brute force: no good for time
        # cont = 0
        # for i in range(1,len(nums)+1):
        #     for j in range(len(nums)-i+1):
        #         #print(j,i,nums[j:j+i], reduce(lambda x, y: x * y, nums[j:j+i]),cont)
        #         if reduce(lambda x, y: x * y, nums[j:j+i]) < k:
        #             cont +=1
        # return cont
        
        
        
        
        
        
        
        # sliding window:  left, right
        #   first:
        #   while  right < len(nums)
        #   if mult(num[left:right]) < k  ->cont +=1, right +=1 
        #   else   left +=1 
        #   if left == right -> right +=1
        #   
        #   finish: 
        #   while left < len(nums): 
        #   if mult(num[left:right]) < k  ->cont +=1, left +=1 
        
#         left = 0
#         right = 1
#         cont = 0
        
#         def is_mult_less(arr,n = k):
#             return reduce(lambda x, y: x * y, arr) < n
        
        
#         while right < len(nums):
#             print(left,right,nums[left:right], is_mult_less(nums[left:right]), reduce(lambda x, y: x * y, nums[left:right]),cont)
            
#             if is_mult_less(nums[left:right]): 
#                 cont  +=(right-left+1)
#                 right +=1 
#             else:
#                 left +=1
#                 right = left +1 
                    
#         while left < len(nums): 
#             print(left,right,nums[left:right], is_mult_less(nums[left:right]), reduce(lambda x, y: x * y, nums[left:right]),cont)
            
#             if is_mult_less(nums[left:right]): 
#                 cont  +=(right-left+1)
#             left  +=1
                
#         return cont



        res = 0 
        l = 0
        product = 1
        for r in range(len(nums)):
            product *= nums[r]
            
            while l <= r and product >= k:
                product = product // nums[l]
                l +=1
                
            res += (r-l+1)

        return res
        
    
    
    
    
    
    