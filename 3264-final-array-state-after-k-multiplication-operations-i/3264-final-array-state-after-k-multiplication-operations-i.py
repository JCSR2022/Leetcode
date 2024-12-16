class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        #aproach: heap nlog(n)
        heap = [ (n,i) for i,n in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            n,i = heapq.heappop(heap)
            nums[i] = n*multiplier
            heapq.heappush(heap,(nums[i],i))
            
        return nums
            
        
        