class Solution:
    def isGood(self, nums: List[int]) -> bool:

        #brute force?,

        if len(nums)<2:
            return False

        nums.sort()
        
        for i,n in enumerate(nums[:-1]):
            if i+1 != n:
                return False

        if  nums[-2] != nums[-1]:
            return False
        
        return True


        