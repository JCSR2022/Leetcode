class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # for i in range(len(nums)-1):
        #     if nums[i] in nums[i+1:i+1+k]:
        #         return True
        # return False
        
        count = {}
        for i, n in enumerate(nums):
            if n in count.keys() and i - count[n] <= k:
                return True
            else:
                count[n] = i
        
        return False