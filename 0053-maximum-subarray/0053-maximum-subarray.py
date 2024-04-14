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
        
        max_current = max_global = nums[0]
        #print(0,nums[0],max_current,max_global)
        for i in range(1,len(nums)):
            max_current = max(nums[i], max_current+nums[i])
            max_global = max(max_global,max_current)
            #print(i,nums[0:i+1],max_current,max_global)
            
        return max_global
            
        
        
        
        return 0
        
        
            
        