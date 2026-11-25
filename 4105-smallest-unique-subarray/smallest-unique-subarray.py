class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:

        MOD = 1000000007
        BASE = 911382323

        n = len(nums)
        h = [0] * (n + 1)
        p = [0] * (n + 1)
        p[0] = 1

        # Compute prefix hashes and powers of BASE
        for i in range(n):
            h[i + 1] = (h[i] * BASE + nums[i]) % MOD
            p[i + 1] = p[i] * BASE % MOD

        def check(length):
            cnt = {}
            for l in range(n - length + 1):
                r = l + length
                key = (h[r] - h[l] * p[length] % MOD + MOD) % MOD
                cnt[key] = cnt.get(key, 0) + 1

            for times in cnt.values():
                if times == 1:
                    return True
            return False

        lo, hi = 1, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
















        # #binary search
               
        # nums_len = len(nums)

        # def checkSubArr(size):
        #     viewSubs = defaultdict(int)
        #     i = 0
        #     while i+size-1 < nums_len:
        #         viewSubs[ "".join([ str(n) for n in  nums[i:i+size] ])   ] +=1
        #         i +=1

        #     for v in viewSubs.values():
        #         if v == 1:
        #             return True
        #     return False

                
        # l = 1
        # r = nums_len
        # while l<=r:
        #     m = (l+r)//2
        #     if checkSubArr(m):
        #         r = m-1
        #     else:
        #         l = m+1
        # return l











#vete a la mierda, no se porque no funciona




#         #binary search
               
#         nums_len = len(nums)

#         def checkSubArr(size):
#             viewSubs = defaultdict(int)
#             i = 0
#             while i+size-1 < nums_len:
#                 viewSubs[ tuple(nums[i:i+size] )] +=1
#                 i +=1

#             for v in viewSubs.values():
#                 if v == 1:
#                     return True
#             return False

                
#         l = 1
#         r = nums_len
#         while l<=r:
#             m = (l+r)//2
#             if checkSubArr(m):
#                 r = m-1
#             else:
#                 l = m+1
#         return l

# #Memory Limit Exceeded

















#----------------------------------------------------
        #brute force like you!!!

        # nums_len = len(nums)

        # def checkSubArr(size):

        #     viewSubs = defaultdict(int)
        #     i = 0
        #     while i+size-1 < nums_len:
        #         viewSubs[ tuple(nums[i:i+size] )] +=1
        #         i +=1

        #     for v in viewSubs.values():
        #         if v == 1:
        #             return True
        #     return False

                
        # for i in range(1,nums_len):
        #     if checkSubArr(i):
        #         return i
        

        # return nums_len





            
        