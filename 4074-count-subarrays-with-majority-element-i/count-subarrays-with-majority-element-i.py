class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:

        #brute force  1000**2

        # ans = 0
        # size = len(nums)
        # for i in range(size):
        #     cnt_target = 0
        #     for j in range(i,size):
        #         if nums[j] == target: cnt_target += 1
        #         if cnt_target > (j-i+1)//2: ans += 1
        # return ans



        #    i    cnt_target     cnt+1      j       nums[j]
        #    0          0           1       0       1
        #    0          1           2       1       2
        #    0          2           3       2       2
#----------------------------------------------------------------------






#-------------------------------------------------------------------------------------------------
#this is more eficcient but i dont understand

        n = len(nums)
        t = target
        cnt = [0] * (n*2+2)
        acc = [0] * (n*2+2)
        pre = n+1
        cnt[pre]=1
        acc[pre]=1
        res =0
        for num in nums:
            if t==num:
                pre+=1
            else:
                pre-=1
            cnt[pre]+=1
            acc[pre] = acc[pre-1] + cnt[pre]
            res+=acc[pre-1]
        return res


