class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:

        N = len(nums)
        ans = 0 
        for i in range(N-1):
            ans = max(ans,abs(nums[i]-nums[i+1]))
        return max(ans,abs(nums[0]-nums[-1]))
        