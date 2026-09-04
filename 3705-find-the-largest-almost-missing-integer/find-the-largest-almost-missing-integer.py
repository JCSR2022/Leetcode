class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:

        if k == len(nums):
            return max(nums)

        if k == 1:
            cnt = Counter(nums)
            for key in sorted(cnt.keys(), reverse =True):
                if cnt[key] ==1:
                    return key
            return -1 


        opc1 = nums[0]
        opc2 = nums[-1]

        cnt_opc1 = 0
        cnt_opc2 = 0
        
        for n in nums:
            cnt_opc1 +=  n == opc1
            cnt_opc2 +=  n == opc2
        
        if cnt_opc1>1:
            opc1 = -1
        if cnt_opc2>1:
            opc2 = -1

        return max(opc1,opc2)

#maldito imbecil!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#--------------------------------------------------------

















