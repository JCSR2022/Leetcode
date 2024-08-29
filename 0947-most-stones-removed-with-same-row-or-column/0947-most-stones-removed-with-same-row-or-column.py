class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        #dfs sol
        
        graph = defaultdict(list)
        
        my_ref = 10000
        
        for i,j in stones:
            graph[i].append((i,j))
            #can not use graph[j], can use graph[~j] or
            #graph[my_ref+j] the important is to build hash
            graph[~j].append((i,j))
        
        # for k,v in graph.items():
        #     print(k,v)
        # return 1
        
        visited = set()
        groups = 0
        
        for i,j in stones:
            if (i,j) not in visited:
                groups += 1
                stack = [(i,j)]
                visited.add((i,j))
                
                while stack:
                    cur_i,cur_j = stack.pop()
                    
                    for new_i,new_j in graph[cur_i]:
                        if (new_i,new_j) not in visited:
                            stack.append((new_i,new_j))
                            visited.add((new_i,new_j))
                            
                    for new_i,new_j in graph[~cur_j]:
                        if (new_i,new_j) not in visited:
                            stack.append((new_i,new_j))
                            visited.add((new_i,new_j))       
                            
        return len(stones) - groups
        