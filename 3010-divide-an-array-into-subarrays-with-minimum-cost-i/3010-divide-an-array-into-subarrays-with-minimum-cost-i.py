class Solution:
    def minimumCost(self, nums: List[int]) -> int:


        if len(nums) == 3:
            return sum(nums)

        most_min = nums[0]

        first_min = min(nums[1:])
        first_min_idx = nums[1:].index(first_min) + 1
        #print(first_min_idx,nums[1:],first_min )

        second_min = min(nums[1:first_min_idx]+nums[first_min_idx+1:])
        #print(nums[1:first_min_idx]+nums[first_min_idx+1:],second_min )
        
        return most_min + first_min +  second_min 
        