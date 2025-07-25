class Solution:
    def maxSum(self, nums: List[int]) -> int:

        return sum([ n for n in set(nums) if n > 0] )
        