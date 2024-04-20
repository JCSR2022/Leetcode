class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # min T of sorting is nLog(n) so sorting is not the way
        #binary search aproach
        
        
        if len(nums) == 1:
            return 0
            
        
        l = 0
        r = len(nums)-1
        
        while l <= r:
            m =   r - (r-l)//2    # (l+r)//2

            # left neighbor check
            if m > 0 and nums[m] < nums[m-1]:
                r = m - 1

            # right neighbor check
            elif m < len(nums)-1 and nums[m] < nums[m+1]:
                l = m + 1

            else:
                return m