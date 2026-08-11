class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        

        maxVal = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i-1]+1:
            maxVal += nums[i]
            i +=1

        set_nums = set(nums)
        while maxVal in set_nums:
            maxVal +=1

        return maxVal