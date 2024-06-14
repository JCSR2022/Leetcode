class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        #brute force
        # create a vistVal arr check if n is in visit, incremet until is not
        # visitVal = []
        # ans = 0
        # for n in nums:
        #     while n in visitVal:
        #         n += 1
        #         ans += 1
        #     visitVal.append(n)
        # #print(visitVal,nums)
        # return ans
        
        
        #https://www.youtube.com/watch?v=XPPs2Wj2YSk
        
        nums.sort()
        res = 0
        
        for i in range(1,len(nums)):
            if nums[i -1] >= nums[i]:
                res += 1 + nums[i-1]-nums[i]
                nums[i] = nums[i-1] + 1
                
        return res
            
        
        
        
        
        