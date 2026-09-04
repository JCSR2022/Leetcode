class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        size = len(nums)

        maxPrefix = [nums[0]]
        for i in range(1,size):
            maxPrefix.append(max(maxPrefix[-1],nums[i]))

        minPrefix = [nums[-1]]
        for i in range(size-2,-1,-1):
            minPrefix.append(min(minPrefix[-1],nums[i]))

        #minPrefix[:] = minPrefix[::-1]
        # ans = [ c_max-c_min for c_max,c_min in zip(maxPrefix,minPrefix)   ]        
        # for i in range(size):
        #     if ans[i] <= k:
        #         return i

        for i in range(size):
            if maxPrefix[i] - minPrefix[size-i-1] <= k:
                return i

        return -1
    


        