class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
       
        #https://www.youtube.com/watch?v=FfJtpOIZXiw

        nums.sort()
        n = len(nums)
        ans = 0

        #target in the arr:
        frec_map = defaultdict(int)
        l = 0
        r = 0
        for x in nums:
            #update sliding window
            while  r < n and nums[r] <= x + k:
                frec_map[nums[r]] += 1
                r += 1
            while l < n and nums[l] < x - k:
                frec_map[nums[l]] -= 1
                l +=1
            #update ans
            max_ops = r - l - frec_map[x]
            ans = max( ans , min(max_ops,numOperations) +frec_map[x] )

        #target is not in the arr:
        l = 0
        for r in range(n):
            #update sliding window
            while l < n and nums[l] + (k*2) < nums[r]:
                l += 1
            
            #update ans
            max_ops = r - l + 1
            ans = max(ans, min(max_ops,numOperations))

        return ans
            


