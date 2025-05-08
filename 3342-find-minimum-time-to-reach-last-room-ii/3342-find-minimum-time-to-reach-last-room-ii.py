class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
        #aproach minheap like disjskra... O(n*log(n))

        n = len(moveTime)
        m = len(moveTime[0])

        heap = []
        heapq.heappush(heap, (0,0,0,True))
        #heap >>>> (time,coordenate_x,coordenate_y,one_sec = True/False)
        visited =set((0,0))

        while heap:
            #print(heap)
            time,i,j,one_sec =  heapq.heappop(heap)

            if i == n-1 and j == m-1:
                return max(moveTime[i][j]+1,time)

            neighbors = [(x,y) for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)] 
                        if x>=0 and y>=0 and x<n and y<m and (x,y) not in visited]
                    
            for neigh_i,neigh_j in neighbors:
                visited.add((neigh_i,neigh_j))
                new_time = max(time,moveTime[neigh_i][neigh_j]) + (1 if one_sec else 2) 
                heapq.heappush(heap, (new_time,neigh_i,neigh_j,not one_sec ))

        return -1
            






