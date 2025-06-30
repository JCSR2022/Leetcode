class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        #worst case O(nLog(n))

        # hash_nums = Counter(nums)
        # values = sorted(hash_nums.keys())

        # max_count = 0 
        # for i in range(1,len(values)):
        #     if values[i]-values[i-1] == 1:
        #         max_count = max(max_count,hash_nums[values[i]]+hash_nums[values[i-1]])
        
        # return max_count
#------------------------------------------------------------------
        
        #no need to sort
        
        hash_nums = Counter(nums)
        max_count = 0 
        for n in hash_nums:
            if n+1 in hash_nums :
                max_count = max(max_count,hash_nums[n]+hash_nums[n+1])
        return max_count