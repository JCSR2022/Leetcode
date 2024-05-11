class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        
#         ratio = [ [q,w/q] for w,q in zip(wage,quality)]
#         ratio = sorted(ratio, key=lambda x: x[1],reverse =True)
#         #print(ratio)
    
#         min_total = float('inf')
#         for i in range(len(ratio)):
#             for j in range(i+1,len(ratio)):
#                 print(ratio[i][0]*ratio[i][1],ratio[j][0]*ratio[i][1],ratio[i][0]*ratio[i][1]+ratio[j][0]*ratio[i][1])
#                 min_total = min(min_total,ratio[i][0]*ratio[i][1]+ratio[j][0]*ratio[i][1])
                
#         return min_total


        res = float("inf")
    
        pairs = [ [w/q,q] for w,q in zip(wage,quality)]
        pairs = sorted(pairs, key=lambda x: x[0])
        
        maxHeap = []
        total_quality = 0
        for rate, q in pairs:
            heapq.heappush(maxHeap,-q)
            total_quality += q
            
            if len(maxHeap) > k :
                total_quality += heapq.heappop(maxHeap)
            
            if len(maxHeap) == k :
                res = min(res,total_quality*rate)
            
    
        
        return res
        
        