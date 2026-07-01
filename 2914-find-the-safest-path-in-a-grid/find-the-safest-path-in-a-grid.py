class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        # n = len(grid)
        # matrix = [[float('inf')]*n for _ in range(n)]

        # def expand(i,j):
    
        #     dq = deque([(i,j,0)])
        #     visited = set()

        #     while dq:
        #         curr_i,curr_j,curr_val = dq.popleft() 
        #         visited.add((curr_i,curr_j))
        #         matrix[curr_i][curr_j] = curr_val 

        #         for mi,mj in [(0,1),(0,-1),(1,0),(-1,0)]:
        #             new_i = curr_i+mi
        #             new_j = curr_j+mj
        #             if (new_i >=0 and 
        #                 new_i < n and 
        #                 new_j >=0 and 
        #                 new_j <n  and 
        #                 (new_i,new_j) not in visited and
        #                 matrix[new_i][new_j] < curr_val+1):

        #                 dq.append((new_i,new_j,curr_val+1))    

        # for i in range(n):
        #     for j in range(n):
        #         if grid[i][j]==1:
        #             expand(i,j)

        
        # for row in matrix:
        #     print(row)

        # return 2
                                

#eres un mnaldito imbecil inutil!!!!!!!!!!!!!!!!1
#------------------------------------------------------------

        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        score = [[float('inf')] * n for _ in range(n)]

        q = deque()

        # Finding all thieves
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    score[i][j] = 0
                    q.append((i, j))

        # Multi-source BFS
        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (0 <= nx < n and 0 <= ny < n and
                        score[nx][ny] > score[x][y] + 1):
                    score[nx][ny] = score[x][y] + 1
                    q.append((nx, ny))

        visited = [[False] * n for _ in range(n)]

        # Max Heap using negative values
        pq = [(-score[0][0], 0, 0)]

        while pq:
            neg_safe, x, y = heapq.heappop(pq)
            safe = -neg_safe

            if x == n - 1 and y == n - 1:
                return safe

            if visited[x][y]:
                continue

            visited[x][y] = True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (0 <= nx < n and 0 <= ny < n and
                        not visited[nx][ny]):

                    new_safe = min(safe, score[nx][ny])
                    heapq.heappush(pq, (-new_safe, nx, ny))

        return -1



            



        