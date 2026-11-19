class Solution:
    def minimizeSum(self, nums: List[int]) -> int:

        # nums[nums.index(max(nums))] = min(nums)
        # print(nums)
        # nums[nums.index(max(nums))] = min(nums)
        # print(nums)
        # return max(nums)-min(nums)

        #no imbecil


        return min(map(sub, nlargest(3, nums), reversed(nsmallest(3, nums)))) 