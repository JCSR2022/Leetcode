class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:

        #brute force  1000**2

        ans = 0
        size = len(nums)
        for i in range(size):
            cnt_target = 0
            for cnt,j in enumerate(range(i,size)):
                if nums[j] == target: cnt_target += 1
                if cnt_target > (cnt+1)//2: ans += 1


        return ans



        #    i    cnt_target     cnt+1      j       nums[j]
        #    0          0           1       0       1
        #    0          1           2       1       2
        #    0          2           3       2       2