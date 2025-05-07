class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        #aproach min heap

        # n = len(moveTime)
        # m = len(moveTime[0])

        # heap = [(0,0,0)]
        # visited = set()
        # while heap:
        #     #print(heap,visited)
        #     time,i,j = heapq.heappop(heap)
        #     visited.add((i,j))

        #     if i == n-1 and j == m-1:
        #         return max(moveTime[i][j]+1,time)
        #     adjacent_rooms = [ (x,y) for x,y in  [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]
        #               if x >= 0  and x < n and y >= 0 and y < m and (x,y) not in visited ]
            
        #     for adj_i,adj_j in adjacent_rooms:
        #         if moveTime[adj_i][adj_j] >= time+1:
        #             heapq.heappush(heap,(moveTime[adj_i][adj_j]+1,adj_i,adj_j))
        #         else:
        #             heapq.heappush(heap,(time+1,adj_i,adj_j))

#Noooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#Time Limit Exceeded
#-------------------------------------------------------------------------   


        n = len(moveTime)
        m = len(moveTime[0])

        heap = [(0,0,0)]
        visited = set()
        while heap:
            #print(heap,visited)
            time,i,j = heapq.heappop(heap)
            visited.add((i,j))

            if i == n-1 and j == m-1:
                return max(moveTime[i][j]+1,time)
            adjacent_rooms = [ (x,y) for x,y in  [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]
                      if x >= 0  and x < n and y >= 0 and y < m and (x,y) not in visited ]
            
            for adj_i,adj_j in adjacent_rooms:
                new_t = max( moveTime[adj_i][adj_j], time) +1
                heapq.heappush(heap,(new_t,adj_i,adj_j))
                

 










