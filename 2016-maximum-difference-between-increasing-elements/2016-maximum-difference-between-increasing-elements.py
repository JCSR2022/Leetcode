class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        #Slading window

        N = len(nums)
        max_dif = -1
        min_val = nums[0]
        for j in range(1,N):
            if nums[j] < min_val:
                min_val = nums[j]
            if nums[j] > min_val:
                max_dif = max(max_dif,nums[j]-min_val)     
    
        return max_dif