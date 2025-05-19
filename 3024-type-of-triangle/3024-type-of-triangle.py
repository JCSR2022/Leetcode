class Solution:
    def triangleType(self, nums: List[int]) -> str:


        if nums[0]+nums[1] > nums[2] and nums[1]+nums[2] > nums[0] and nums[0]+nums[2] > nums[1]:

            set_nums = set(nums)
        
            if len(set_nums) == 1:
                return "equilateral"

            elif len(set_nums) == 2:
                return "isosceles"

            else:
                return   "scalene"

        else:
            return "none"
        