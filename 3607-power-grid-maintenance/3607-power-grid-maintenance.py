from sortedcontainers import SortedList

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        # make arr connect_status size c-1, if connect_status[i-1] is True, return i
        # make adj_list with sortedlists?? , if status False, return min of adj_list[i-1], if not return -1
        # when turn off, modify all adj_list[i-1] 

    
        # connect_status = [True]*c

        # adj_list = defaultdict(SortedList)
        # for st1,st2 in connections:
        #     adj_list[st1].add(st2)
        #     adj_list[st2].add(st1)

        # print(dict(adj_list))

        # return [1,2,3]                        

#nooooooo, incorrect logic
#--------------------------------------------------------------

        #secund aproach:
        # somthing like union find???
        
#noooo
#----------------------------------------------------------

        #try somthing lik disjkra???
        #not needed, just find grid and return min active on grid
        #in fact you can convert grid as heap, return min always if no heap return -1
        
        
        adjList = defaultdict(set)
        for st1,st2 in connections:
            adjList[st1-1].add(st2-1)
            adjList[st2-1].add(st1-1)

    
        #simple BFS!!!!
        def bfs(adjList, node):
            visited = set()
            visited.add(node)
            q = deque([node])

            while q:
                curr_node = q.popleft()
                if curr_node in adjList:
                    for neigh in  adjList[curr_node]:
                        if neigh not in visited:
                            visited.add(neigh)
                            q.append(neigh)    
            return visited


        grids = defaultdict(SortedList)
        station_grid = defaultdict(int)
        grid_num = 0
        stations = set()
        for sta in range(c):
            if sta not in stations:
                curr_grid = bfs(adjList, sta)
                for curr_sta in curr_grid:
                    grids[grid_num].add(curr_sta)
                    station_grid[curr_sta] = grid_num
                grid_num +=1
                stations.update(curr_grid)
        
      

        connect_status = [True]*c

        # print(dict(grids))            
        # print()
        # print(dict(station_grid))
        # print()
        # print(connect_status)

        ans =[]
        for qr,q_sta in queries:
            if qr == 1:
                if connect_status[q_sta-1]:
                    ans.append(q_sta)
                else:
                    sta_grid = station_grid[q_sta-1]
                    if grids[sta_grid]:
                        ans.append(grids[sta_grid][0]+1)
                    else:
                        ans.append(-1)

            elif qr == 2:
                if connect_status[q_sta-1]: 
                    connect_status[q_sta-1] = False
                    sta_grid = station_grid[q_sta-1]
                    grids[sta_grid].remove(q_sta-1)

        return ans



















