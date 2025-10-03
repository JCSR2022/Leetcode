class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # rows,cols = len(heightMap), len(heightMap[0])

        # def find_neighbors(i,j):
        #     neigh = []

        #     if i > 0:
        #         neigh.append([i-1,j])
        #     if i < rows-1:
        #         neigh.append([i+1,j])
        #     if j > 0:
        #         neigh.append([i,j-1])
        #     if j < cols-1:
        #          neigh.append([i,j+1])
            
        #     return neigh


        # heap = []
        # for r in range(rows):
        #     for c in range(cols):
        #         #only include borders
        #         if r in [0 ,rows-1] or c in [0,cols-1]:
        #             heappush(heap,(heightMap[r][c],r,c))
        #             #visited
        #             heightMap[r][c] = -1

        # ans = 1
        # max_h = -1

        # while heap:
        #     h,r,c = heappop(heap)
        #     max_h = max(max_h,h)
        #     ans += max_h - h

        #     #[[r+1,c],[r-1,c],[r,c+1],[r,c-1]]
        #     neighbors = find_neighbors(r,c)
  
        #     for neigh_r,neigh_c in neighbors:
        #         if heightMap[neigh_r][neigh_c] == -1:
        #             continue
        #         heappush(heap,(heightMap[neigh_r][neigh_c],neigh_r,neigh_c ))
        #         heightMap[neigh_r][neigh_c] = -1

        # return ans

#no funciona!!!!!!!!!!!!!!!@$%$#^%$^$%&%^*^&*^
#-----------------------------------------------------------------------------------
#An-Wen Deng
#https://www.youtube.com/watch?v=n4Gq0DnT9Oc&t=3s

        dir = (0, 1, 0, -1, 0)
        m, n = len(heightMap), len(heightMap[0])
        if m <= 2 or n <= 2:
            return 0

        boundary = []
        for i in range(m):
            boundary.append((heightMap[i][0], i, 0))
            boundary.append((heightMap[i][-1], i, n - 1))
            heightMap[i][0] = heightMap[i][-1] = -1

        for j in range(1, n - 1):
            boundary.append((heightMap[0][j], 0, j))
            boundary.append((heightMap[-1][j], m - 1, j))
            heightMap[0][j] = heightMap[-1][j] = -1

        heapify(boundary)
        ans, water_level = 0, 0

        while boundary:
            h, i, j = heappop(boundary)

            water_level = max(water_level, h)

            for a in range(4):
                i0, j0 = i + dir[a], j + dir[a + 1]
                if i0 < 0 or i0 >= m or j0 < 0 or j0 >= n or heightMap[i0][j0] == -1:
                    continue
                currH = heightMap[i0][j0]
                if currH < water_level:
                    ans += water_level - currH

                heightMap[i0][j0] = -1
                heappush(boundary, (currH, i0, j0))
        return ans

