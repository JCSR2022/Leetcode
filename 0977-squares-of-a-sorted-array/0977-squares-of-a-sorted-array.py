class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = int(nums[i]**2)
        nums = sorted(nums,reverse = False)
        return nums
        