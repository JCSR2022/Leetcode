from math import gcd
from functools import cache

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:

        MOD = 10**9+7
        size = len(nums)

        @cache
        def dp(i,gcd1,gcd2):

            if i == size:
                if  gcd1 == gcd2 and gcd2 != 0 :
                    return 1
                else:
                    return 0

            
            total = dp(i+1,gcd1,gcd2)                               # no use
            total = (total + dp(i+1,gcd(gcd1,nums[i]),gcd2))%MOD    # use on group 1
            total = (total + dp(i+1,gcd1,gcd(gcd2,nums[i])))%MOD    # use on group 2

            return total 


        return dp(0,0,0)

        