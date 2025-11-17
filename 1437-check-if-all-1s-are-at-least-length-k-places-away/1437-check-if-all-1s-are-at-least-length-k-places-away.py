class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:

        #lest check if this is fast enough:

        if k == 0:
            return True

        s_nums = "".join([str(n) for n in nums]).strip("0")

        if "11" in s_nums:
            return False
        
        for gap in s_nums.split('1'):
            if gap and len(gap) < k:
                return False
        return True 


        # cnt = k
        # for i in range(len(nums)):
        #     if nums[i] == 1 and cnt < k:
        #         return False
        #     else:
        #         if 


        