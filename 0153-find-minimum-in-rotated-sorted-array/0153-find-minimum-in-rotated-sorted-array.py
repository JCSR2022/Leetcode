class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search ?
        
        if len(nums) ==1:
            return nums[0]
        
        L = 0
        R = len(nums)-1
        
        
        while L < R:
            M = (R+L)//2
            #print(nums[L],nums[M],nums[R])
            
            if nums[M+1] >= nums[M] and nums[M-1] >= nums[M]:
                return nums[M]
            
            if nums[R] <= nums[M]:
                L = M + 1
            else:
                R = M - 1
            
        return min(nums[L],nums[M],nums[R])
        
        

        
        
        