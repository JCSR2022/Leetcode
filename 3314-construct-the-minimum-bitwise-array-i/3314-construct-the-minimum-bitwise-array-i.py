class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:





#--------------------------------------------------------------
        #brute like me
        
        size = len(nums)

        ans= [-1]*size

        for i in range(size):
            for n in range(nums[i]):
                if n|(n+1) == nums[i]:
                    ans[i] = n
                    break
        
        return ans
#--------------------------------------------------------------