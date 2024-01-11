class Solution:
    def canJump(self, nums: List[int]) -> bool:
        posibleSalto = True
        
        if 0 not in nums or nums == [0]:
            return posibleSalto 
        
        for i,p in enumerate(nums):
            #print(i,p)
            if p == 0 and i<len(nums)-1:
                posibleSalto = False
                for j in range(i- 1, -1, -1):
                    #print(f"     {i-j,j, nums[j], nums[j]>i-j}  , " )
                    posibleSalto = nums[j]>i-j
                    if posibleSalto: break
                if not posibleSalto: break 
                        
        return posibleSalto 