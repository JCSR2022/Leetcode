class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        dist_arr = [ [-1]*2 for _ in range(len(edges))]

        def dfs(node,node_stu,dist):
            if dist_arr[node][node_stu] == -1:
                dist_arr[node][node_stu] = dist
                if edges[node] != -1:
                    dfs(edges[node],node_stu,dist+1)
        
        dfs(node1,0,0)
        dfs(node2,1,0)
        
        min_dist = float("inf")
        indx = -1
        for i,dist in enumerate(dist_arr):
            if dist[0] == -1 or dist[1] == -1:
                continue
            curr_min = max(dist)
            if curr_min < min_dist:
                min_dist = curr_min
                indx = i

        return indx





#---------------------------------------------------------------------

        #aproach, dfs from node1 and node2 until -1 or node visited
        #find first number on dfs_arr1 that is on dfs_arr2 


        # def dfs(node,dfs_arr):
        #     #return set with nodes on dfs
        #     if node in dfs_arr:
        #         return dfs_arr

        #     dfs_arr.append(node)
        #     if edges[node] == -1:
        #         return dfs_arr

        #     return dfs(edges[node],dfs_arr)

        # dist1 = -1
        # arr1 = dfs(node1,[])
        # print(arr1)
        # if node2 in arr1:
        #     dist1 = arr1.index(node2)
        
        # dist2 =-1
        # arr2 = dfs(node2,[])
        # print(arr2)
        # if node1 in arr2 and dist1 !=-1:
        #     dist2 = arr2.index(node1)
        #     if dist1 < dist2:
        #         return node2
        #     else:
        #         return node1

        # for node in arr1:
        #     if node in arr2:
        #         return node 

        # return -1

#nooooo, maldito imbecil,deberias morirte..
#-----------------------------------------------

        #multi source BFS

        # restriction "each node has at most one outgoing edge"
        # #   makes cnt_nodes = len(edges)

        # N = len(edges)
        # #2 nodes distences
        # dist_arr = [ [-1]*2 for _ in range(N)]
        # def dfs(stud_node,node,dist):
        #     print(dist_arr)
        #     if dist_arr[node][stud_node] == -1:
        #         dist_arr[node][stud_node] = dist
        #         dfs(stud_node,edges[node],dist+1)

        # dfs(0,node1,0)
        # dfs(1,node2,0)
               
        # for node,dist in enumerate(dist_arr):
        #     print(node,dist)

        # return -1

#nooooo, maldito imbecil,deberias morirte..X@@@@@@2weg
#-----------------------------------------------






















