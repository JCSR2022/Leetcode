class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        ans = 0 

        for i in range(1, len(nums)+1):
            elements = [list(x) for x in itertools.combinations(nums, i)]
            #print(elements)
            
            for els in elements:
                xor_total = reduce(lambda x, y: x ^ y, els)
                ans += xor_total
                #print(els,xor_total)
        
        return ans
    
    
    
    
    
    
    