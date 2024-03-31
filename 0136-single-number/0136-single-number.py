class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hastable = {}
        
        for n in nums:
            if n in hastable:
                hastable[n] +=1
            else:
                hastable[n] = 1
                
        for key,val in hastable.items():
            if val == 1:
                return key