class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        # brute aproach  O(n**2):
        
        # maximo = -inf
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)+1):
        #         print(nums[i:j],nums[i:j],maximo)
        #         maximo = max(maximo,sum(nums[i:j]))     
        # return maximo
        
        
        # aproach #1 Kadanes: 
        
#         max_current = max_global = nums[0]
#         print(0,nums[0],max_current,max_global)
#         for i in range(1,len(nums)):
#             max_current = max(nums[i], max_current+nums[i])
#             max_global = max(max_global,max_current)
#             print(i,nums[0:i+1],max_current,max_global)
            
#         return max_global
            
    
    
    
        max_current = max_global = nums[0]
        #print(0,nums[0],max_current,max_global)
        j = k = 0
        for i in range(1,len(nums)):
            max_current = max(nums[i], max_current+nums[i])
            new_max_global = max(max_global,max_current)
            if new_max_global > max_global:
                max_global = new_max_global
                #j = k = i
                #while sum(nums[j:i+1]) != max_global:
                #    j -=1
            #print(i,nums[i],nums[j:k+1],max_current,max_global)
        #subarray_largest_sum = nums[j:k+1] 
        #print("subarray_largest_sum:",subarray_largest_sum)
        return max_global    
    
    
    
    
    
    
    
    
    
    
#         current_Left = 0
#         global_left = 0
#         max_current = nums[current_Left]
#         max_global = nums[global_left]
        
#         for i in range(1,len(nums)):
#             current_right = i
            
#             if  max_current + nums[current_right] > nums[current_right]:
#                 max_current = max_current + nums[current_right]
#             else:
                
            
            
#             max_current = max(nums[i], max_current+nums[i])
            
            
            
#             max_global = max(max_global,max_current)
#             print(i,nums[0:i+1],max_current,max_global)
            
#         return max_global
            
        
            
        