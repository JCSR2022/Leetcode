class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # aproach: n Log(n) (sort the array)
        # two pointers
        #   move through nums from lef to right and from right to left
        
        nums.sort()
        #print(nums)
        
        l = 0
        r = len(nums)-1
        
        while l < r:
            #print(l,r,nums[l],nums[r])
            if -1*nums[l] == nums[r]:
                return nums[r]
            elif abs(nums[l]) > abs(nums[r]):
                l += 1
            else: 
                r -= 1
                
            
        
        return -1
        
        