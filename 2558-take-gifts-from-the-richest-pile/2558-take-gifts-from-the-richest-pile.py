class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        #aproach: maxheap
        
        gifts_heap = [-x for x in gifts]
        heapq.heapify(gifts_heap)

        for _ in range(k):
            num = -1 * heapq.heappop(gifts_heap)
            heapq.heappush(gifts_heap, -1*math.floor(math.sqrt(num)))

            
        return sum([-1*x for x in gifts_heap])
        