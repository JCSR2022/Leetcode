class Solution:
    def minOperations(self, nums: List[int]) -> int:

        #if 1 in nums , ans = len(nums) -count(ones)
        # 
        #min comun mult == 1 then ans = len(nums) -count(ones)

        #no se
#------------------------------------------------------------------
        #https://www.youtube.com/watch?v=WIMtGGTsuCQ

        def gcd(a,b):
            if a%b == 0: return b
            return gcd(b%a,a)

        n = len(nums)
        ones = 0
        current_gcd = 0
        for x in nums:
            current_gcd = gcd(current_gcd,x)
            if x==1:ones += 1
        
        if current_gcd >1: return -1
        elif ones > 0: return n-ones

        min_len = n
        for i in range(n):
            g = 0
            for j in range(i,n):
                g = gcd(g,nums[j])
                if g == 1:
                    min_len = min(min_len,j-i+1)
                    break

        return (min_len -1) + (n-1) 
        


        