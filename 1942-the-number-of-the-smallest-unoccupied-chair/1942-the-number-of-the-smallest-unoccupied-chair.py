class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        
        times = [(a,l,i) for i,(a,l) in enumerate(times)]
        times.sort()
        #times.sort(key=lambda x: x[1])
        #times.sort(key=lambda x: x[0])



        availableChairs = list(range(len(times)))
        heapify(availableChairs)
        usedChairs = []

        for a,l,i in times:
            while usedChairs and usedChairs[0][0] <= a:
                _,idx = heappop(usedChairs)
                heappush(availableChairs,idx)

            cur  = heappop(availableChairs)
            if i == targetFriend:
                return cur
            
            heappush(usedChairs,(l,cur))