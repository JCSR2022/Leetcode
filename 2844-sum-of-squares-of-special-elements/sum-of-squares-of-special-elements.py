class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        size =len(nums)
        ans = 0
        for i,n in enumerate(nums):
            ans += n**2 if size%(i+1) ==0 else 0
        return ans
