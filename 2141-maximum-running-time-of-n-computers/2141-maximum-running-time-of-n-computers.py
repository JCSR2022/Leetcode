class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:


        #brute force aproach:
        # make heap and pop n reduce by 1 all ,repeat until 0//

        heap = []
        for bat in batteries:
            heapq.heappush(heap,-bat) 
        #print(heap)
        count = 0
        while True:
            bat_to_use = []
            for _ in range(n):
                curr_bat = heapq.heappop(heap)
                if curr_bat == 0:
                    return count
                bat_to_use.append(curr_bat+1)
            #print(bat_to_use)
            for bat in bat_to_use:
                heapq.heappush(heap,bat)
            #print(heap)
            count +=1
            





#----------------------------------------------------
        #sum all batteries and // by n??
        #return sum(batteries)//n
#do not work

