class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        
        


        #aproach:
        # find on edeges2 node with max nodes_in_target 
        # find for each node in  edeges1  nodes_in_target
        # add (1) and (2)
        # worst time m**2  + n**2

        n = len(edges1)+1
        m = len(edges2)+1

        #special case
        if k == 0:
            return [1]*n

        #bild trees:
        tree1 = defaultdict(list)
        for ai, bi in edges1:
            tree1[ai].append(bi)
            tree1[bi].append(ai)

        tree2 = defaultdict(list)
        for ui,vi in edges2:
            tree2[ui].append(vi)
            tree2[vi].append(ui)

        #print(dict(tree1))
        #print(dict(tree2))

        # find max on edeges2        
        max_cnt_nodes = 0
        for i in range(m): 
            q = deque()
            curr_cnt_nodes = 0
            q.append((i,1))
            visited = set()
            while q :
                #print(i,list(q),curr_cnt_nodes,max_cnt_nodes)
                node,level =  q.popleft()
                visited.add(node)
                curr_cnt_nodes += 1

                if level+1 > k:
                    continue

                for next_node in tree2[node]:
                    if next_node not in visited:
                        q.append((next_node,level+1))
            max_cnt_nodes = max(max_cnt_nodes,curr_cnt_nodes)
        #print(max_cnt_nodes)

        ## find for each node in  edeges1
        ans = [0]*n
        for i in range(n):
            q = deque()
            curr_cnt_nodes = 0
            q.append((i,1))
            visited = set()
            while q :
                node,level =  q.popleft()
                visited.add(node)
                curr_cnt_nodes += 1

                if level > k:
                    continue

                for next_node in tree1[node]:
                    if next_node not in visited:
                        q.append((next_node,level+1))
            
            ans[i] = curr_cnt_nodes + max_cnt_nodes

        return ans
 
        














        


