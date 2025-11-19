class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:

        #do the size of the arr i think a brute force will work
        nums = set(nums)

        while original in nums:
            original *=2

        return original
        