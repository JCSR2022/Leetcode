class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

            ans = 0
            heap = []
            for i in range(1,len(colors)):
                if colors[i] == colors[i-1]:
                    heapq.heappush(heap, neededTime[i-1])
                else:
                    if heap:
                        heapq.heappush(heap, neededTime[i-1])
                        while len(heap) > 1:
                            ans += heapq.heappop(heap)
                        heapq.heappop(heap)

            heapq.heappush(heap, neededTime[-1])
            while len(heap) > 1:
                ans += heapq.heappop(heap)
                
            return ans






























        # num_ballons = len(neededTime)
        # if num_ballons==1:
        #     return 0

        # list_colors = list(colors)
        # j = 1 
        # group = []
        # sum_time = 0
        # while j < num_ballons:
        #     i = j-1
        #     if list_colors[i] == list_colors[j]:
        #         if group == []:
        #             group = [neededTime[i],neededTime[j]]
        #             #print(i,j,list_colors[i],list_colors[j],neededTime[i],neededTime[j],sum_time,group)
        #             sum_time += min(group)
        #             group.pop(group.index(min(group)))
        #         else:
        #             group.append(neededTime[j])
        
        #             sum_time += min(group)
        #             group.pop(group.index(min(group)))    
        #     else:
        #         group = []
        
        #     j +=1

        # return sum_time
