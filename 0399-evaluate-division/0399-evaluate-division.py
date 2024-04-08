class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj = collections.defaultdict(list)
        
        for i, eq in enumerate(equations):
            a,b = eq
            adj[a].append([b,values[i]])
            adj[b].append([a,1/values[i]])
        
        #for key,val in adj.items():
        #   print('Inc: ',key,val)
        
        
        def bfs(src,target,i):
            if src not in adj or target not in adj:
                return -1
            
            q = deque()
            visit = set()
            
            
            q.append([src,1])
            visit.add(src)
         
            while q:
               # print(f'{i},src:{src},target:{target}=',q,visit )
                n,w = q.popleft()
                if n == target:
                    return w
                for nei,weight in adj[n]:
                    if nei not in visit:
                        q.append([nei, w*weight])
                        visit.add(nei)
            return -1
                
        return [ bfs(qu[0],qu[1],i) for i,qu in enumerate(queries)]
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
            
            
            