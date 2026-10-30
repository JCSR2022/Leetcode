
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:


        # --------------------------------------------------
        # STEP 1: Build adjacency list
        # --------------------------------------------------
        adj_list = defaultdict(list)
        for u, v, w in edges:
            adj_list[u].append((w, v))



        # --------------------------------------------------
        # STEP 2: Initialize distances
        #
        # distance[node][char][count]
        #
        # Stores the minimum cost to reach a node with:
        # - A specific last character
        # - A specific consecutive character count
        # --------------------------------------------------
        distance = [ [[float("inf")] * (k + 1) for _ in range(26)] for _ in range(n) ]

        start_char = ord(labels[0]) - ord('a')

        distance[0][start_char][1] = 0



        # --------------------------------------------------
        # STEP 3: Initialize priority queue
        #
        # (cost, node, last_character, consecutive_count)
        # --------------------------------------------------

        heap = [(0, 0, start_char, 1)]

        # --------------------------------------------------
        # STEP 4: Dijkstra
        # --------------------------------------------------

        while heap:

            curr_weight, curr_node, curr_char, cnt = heapq.heappop(heap)

            # Ignore outdated states
            if curr_weight > distance[curr_node][curr_char][cnt]:
                continue

            # Destination reached
            if curr_node == n - 1:
                return curr_weight

            # Explore neighbors
            for weight, neighbor in adj_list[curr_node]:

                neighbor_char = ord(labels[neighbor]) - ord('a')

                # Calculate consecutive character count
                if neighbor_char == curr_char:
                    new_cnt = cnt + 1
                else:
                    new_cnt = 1

                # The path cannot exceed k consecutive characters
                if new_cnt > k:
                    continue

                new_weight = curr_weight + weight

                # Relaxation: update if a cheaper path is found
                if new_weight < distance[neighbor][neighbor_char][new_cnt]:

                    distance[neighbor][neighbor_char][new_cnt] = new_weight

                    heapq.heappush(
                        heap,
                        (
                            new_weight,
                            neighbor,
                            neighbor_char,
                            new_cnt
                        )
                    )

        # No valid path exists
        return -1












        # #using dijkstra algorithm

        # adj_list = defaultdict(list)
        # for u,v,w in edges:
        #     adj_list[u].append((w,v))

        # distance_to_origen = [ float("inf") ] * n
        # distance_to_origen[0] = 0
        # previos_node = [None] * n

        # myqueue = deque([])
        # visited = set()
        # myqueue.append((0,0,labels[0],1))
        
        # while myqueue:
        #     curr_weight,curr_node,curr_ch,cnt_cons_ch = myqueue.popleft()

        #     if curr_node == n-1 :
        #         return curr_weight

        #     if curr_node in visited:
        #         continue
        #     else:
        #         visited.add(curr_node)

        #     for weight , neighbor_node in  adj_list[curr_node]:
                
                
        #         cond1 = neighbor_node not in visited 
        #         cond2 = weight+curr_weight < distance_to_origen[neighbor_node] 
                
        #         new_cnt_cons_ch =  1 if labels[neighbor_node] != curr_ch else cnt_cons_ch +1
        #         cond3 = new_cnt_cons_ch < k  


        #         if cond1 and cond2 and cond3:
        #             distance_to_origen[neighbor_node] = weight+curr_weight
        #             previos_node[neighbor_node] = curr_node
        #             myqueue.append((weight+curr_weight,neighbor_node,curr_ch,new_cnt_cons_ch))

        # return -1




