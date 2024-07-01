class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        #https://www.youtube.com/watch?v=FXWRE67PLL0
        #Redundant Connection - Union Find 
        # i make my version
        # base on unionFind exmaple: https://www.youtube.com/watch?v=PGZ64ob440I
        
        def findRoot_Size(x,UnionFind):
            if UnionFind[x] < 0 :
                return x,abs(UnionFind[x])
            else:
                return findRoot_Size(UnionFind[x],UnionFind)

        def union(x,y,UnionFind):
            x,size_x = findRoot_Size(x,UnionFind)
            y,size_y = findRoot_Size(y,UnionFind)

            if size_x >= size_y:
                UnionFind[y] = x
                UnionFind[x] = -1*(size_x+size_y)
            else:
                UnionFind[x] = y
                UnionFind[y] = -1*(size_x+size_y)
        
        def isRemoveEdge(x,y):
            x,size_x = findRoot_Size(x,UnionFind)
            y,size_y = findRoot_Size(y,UnionFind)
            
            if x == y and x != -1:
                return True
            
            return False

        
        # nodes[0]=0 wont be use
        nodes = len(edges)+1
        
        UnionFind = [-1]*nodes
        
        for x,y in edges:
            if isRemoveEdge(x,y):
                return [x,y]
            union(x,y,UnionFind)
        
        
        