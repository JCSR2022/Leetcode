class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        #brute force:
                
        
#         ans = [True]*len(queries)
#         for i,(from_i, to_i) in enumerate(queries):

#             for j in range(from_i, to_i):
#                 if nums[j]%2 == nums[j+1]%2:
#                     ans[i] = False
#                     break
                                
#         return ans
    
    #--------------------------------------------
    #using prefix
    
        prefix = [0]*len(nums)
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]
            if nums[i-1]%2 == nums[i]%2:
                prefix[i] += 1  

        ans = []
        for from_i, to_i in queries:
            ans.append(prefix[from_i] == prefix[to_i])   
            
        # ans = [True]*len(queries)
        # for i,(from_i, to_i) in enumerate(queries):
        #     ans[i] = prefix[from_i] == prefix[to_i]            
            
        return ans  
    
    
    
            
            