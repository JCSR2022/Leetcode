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

#Time Limit Exceeded
#-------------------------------------------------------------------------   


        # n = len(moveTime)
        # m = len(moveTime[0])

        # heap = [(0,0,0)]
        # visited = set()
        # while heap:
        #     print(heap)
        #     time,i,j = heapq.heappop(heap)
        #     visited.add((i,j))

        #     if i == n-1 and j == m-1:
        #         return max(moveTime[i][j]+1,time)
            
        #     adjacent_rooms = [ (x,y) for x,y in  [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]
        #               if x >= 0  and x < n and y >= 0 and y < m and (x,y) not in visited ]
            
        #     for adj_i,adj_j in adjacent_rooms:
        #         new_t = max(moveTime[adj_i][adj_j], time) +1
        #         heapq.heappush(heap,(new_t,adj_i,adj_j))
                
#no se porque mierda no funciona!!!!!!
#-----------------------------------------------------


        # n = len(moveTime)
        # m = len(moveTime[0])

        # dp = [[float('inf')] * m for _ in range(n)]
        # minh = []
        # heapq.heappush(minh, (0, 0, 0))
        # moveTime[0][0] = 0
        # directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # while minh:
        #     currTime, currRow, currCol = heapq.heappop(minh)
        #     if currTime >= dp[currRow][currCol]:
        #         continue
        #     if currRow == n - 1 and currCol == m - 1:
        #         return currTime
        #     dp[currRow][currCol] = currTime
        #     for dr, dc in directions:
        #         nextRow = currRow + dr
        #         nextCol = currCol + dc
        #         if 0 <= nextRow < n and 0 <= nextCol < m and dp[nextRow][nextCol] == float('inf'):
        #             nextTime = max(moveTime[nextRow][nextCol], currTime) + 1
        #             heapq.heappush(minh, (nextTime, nextRow, nextCol))
        # return -1

#-------------------------------------------------------------------


        n = len(moveTime)
        m = len(moveTime[0])

        heap = [(0,0,0)]
        dp = {(0,0):0}
        while heap:
            #print(heap,dp)
            time,i,j = heapq.heappop(heap)

            # if (i,j) in dp and dp[(i,j)] < time:
            #     continue 

            if i == n-1 and j == m-1:
                return max(moveTime[i][j]+1,time)
            
            adjacent_rooms = [ (x,y) for x,y in  [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]
                      if x >= 0  and x < n and y >= 0 and y < m and (x,y) not in dp ]
            
            for adj_i,adj_j in adjacent_rooms:
                new_t = max(moveTime[adj_i][adj_j], time) +1
                dp[(adj_i,adj_j)] = new_t
                heapq.heappush(heap,(new_t,adj_i,adj_j))



