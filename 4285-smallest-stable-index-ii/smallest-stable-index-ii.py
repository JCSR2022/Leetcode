class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        size = len(nums)

        pre_max = [nums[0]]*size
        for i in range(1,size):
            pre_max[i] = max(pre_max[i-1],nums[i])
        
        pre_min = [nums[-1]]*size
        for i in range(size-2,-1,-1):
            pre_min[i] = min(pre_min[i+1],nums[i])

        for i in range(size):
            if pre_max[i]-pre_min[i] <= k :
                return i

        return -1    

        