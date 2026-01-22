class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:

        #brute force , realy brute

        ans = 0
        Order = False
        changes = 0
        while not Order and len(nums) > 1:
            indxPair = 1
            Par_val = float("inf")
            Order = True

            for i in range(1,len(nums)):
                if nums[i] < nums[i-1]:
                    Order = False
                if nums[i] + nums[i-1] < Par_val:
                    Par_val = nums[i] + nums[i-1]                
                    indxPair = i
            
            if not Order:
                ans += 1
                nums = nums[:indxPair-2]+[Par_val]+nums[indxPair+1:]

        return ans