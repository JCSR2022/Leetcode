class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:

        #do the size of the arr i think a brute force will work
        # nums = set(nums)

        # while original in nums:
        #     original *=2

        # return original
#------------------------------------------------------------------

        nums.sort()
        high = len(nums)
        i = bisect.bisect_left(nums,original)
        
        while i < high:
            print(i,nums[i],original == nums[i])
            if original == nums[i]:
                original *= 2
            else:
                return original
            i = bisect.bisect_left(nums,original,i,high)

        return original


#----------------------------------------------------------------




