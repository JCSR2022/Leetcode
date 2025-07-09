class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        #aproach O(n)
        #create max_heap_gap with values  
        # [startTime[0]]
        # + [endTime[i-1] - startTime[i] for i in range(1,N)] + 
        # + [eventTime - endTime[-1]] 
        # pop k times


        gaps = []

        start = startTime[0]
        if start > 0:
            heapq.heappush(gaps,-start)
            #print("start:",gaps)

        end = eventTime - endTime[-1]  
        if end > 0:
            heapq.heappush(gaps,-end)
            #print("end:",gaps)
        

        for i in range(1,len(startTime)):
            curr_gap = startTime[i] - endTime[i-1]
            if curr_gap > 0:
                heapq.heappush(gaps,-curr_gap)
            #print("curr_gap:",(endTime[i-1],startTime[i]),curr_gap,gaps)

            
        #print(gaps)
        if not gaps:
            return 0

        moves = 0
        ans = 0
        while gaps and moves <= k :
            ans += -heapq.heappop(gaps)
            moves += 1

        return ans
    




