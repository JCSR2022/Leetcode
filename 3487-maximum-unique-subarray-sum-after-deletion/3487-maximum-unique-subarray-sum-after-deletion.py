class Solution:
    def maxSum(self, nums: List[int]) -> int:
        unique = set(nums)
        pos_ans = [ n for n in set(nums) if n > 0]
        if pos_ans:
            return sum(pos_ans)
        else:
            return max(unique)
        