class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)+1):
#                 print(nums[i:j])
                
#         return 0

#        import itertools

        ans = 0 

        for i in range(1, len(nums)+1):
            elements = [list(x) for x in itertools.combinations(nums, i)]

            #print(elements)
            
            for els in elements:
                xor_total = reduce(lambda x, y: x ^ y, els)
                ans += xor_total
                #print(els,xor_total)
        
        return ans
    
    
    
    
    
    
    