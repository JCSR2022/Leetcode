class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        #heap

        minheap = []
        for n in nums:
            heapq.heappush(minheap,-n)
            
        ans = 0
        for _ in range(k):
            n = -heapq.heappop(minheap)
            ans += n
            heapq.heappush(minheap, -math.ceil(n/3))
        return ans




#         for i in range(len(nums)):
#             nums[i] = -nums[i]    
        
#         heapify(nums)
#         ans = 0
#         for _ in range(k):
#             n = -heapq.heappop(nums)
#             #print(nums,n,ans)
#             ans += n
#             heapq.heappush(nums, -math.ceil(n/3))
#         return ans