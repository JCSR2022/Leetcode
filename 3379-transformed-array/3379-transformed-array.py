class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        size = len(nums)

        return [ nums[(i+n+size)%size] for i,n in enumerate(nums)]

        
        #result = [ n for n in nums]
        #for i in range(size):
        #    if nums[i]>0:
        #        result[i] = nums[(i+nums[i])%size]
        #    elif nums[i]<0:
        #        result[i] = nums[(i+nums[i]+size)%size]

        #return result
        