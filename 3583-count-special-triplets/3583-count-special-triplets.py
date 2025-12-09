class Solution:
    def specialTriplets(self, nums: List[int]) -> int:

        # MOD = 10**9+7
        # num_indx = defaultdict(list)

        # ans = 0
        # for k,n in enumerate(nums):
        #     if n%2 ==0 and n in num_indx and n//2 in num_indx:
        #         #this can be improve with binary search
        #         #print(k,n,(num_indx[n],[nums[x] for x in num_indx[n]]),(num_indx[n//2],[nums[x] for x in num_indx[n//2]])  )
        #         for j in num_indx[n//2]:
        #             ans += sum( 1 for i in num_indx[n] if i<j )
        #         #print("ans:",ans)
        #     num_indx[n].append(k)

        # return ans%MOD

#Time Limit Exceeded test case 1114
#-----------------------------------------------------------

        MOD = 10**9+7
        total_freq = Counter(nums)
        left_frec = defaultdict(int)
        ans = 0

        for n in nums:
            if n*2 in left_frec:
                ans += left_frec[n*2]*(total_freq[n*2] -left_frec[n*2] - (1 if n==0 else 0) )
                ans %=MOD
            #print(dict(total_freq),dict(left_frec),ans )
            left_frec[n] +=1

        return ans 
