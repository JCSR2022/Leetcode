class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        for i in range(len(nums)-1):
            if nums[i] in nums[i+1:i+1+k]:
                return True
        return False
        