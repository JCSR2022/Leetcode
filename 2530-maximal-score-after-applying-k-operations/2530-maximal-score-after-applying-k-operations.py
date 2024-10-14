class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        #heap
        
        for i in range(len(nums)):
            nums[i] = -nums[i]    
        
        heapify(nums)
        ans = 0
        for _ in range(k):
            n = -heapq.heappop(nums)
            #print(nums,n,ans)
            ans += n
            heapq.heappush(nums, -math.ceil(n/3))
        return ans