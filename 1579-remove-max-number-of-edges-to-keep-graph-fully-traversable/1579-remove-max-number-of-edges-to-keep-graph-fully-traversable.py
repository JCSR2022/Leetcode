class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        
        
#lancertech6
#https://www.youtube.com/watch?v=LfaQjcE_LEM

# UnionFind class definition
        class UnionFind:
            def __init__(self, n):
                self.representative = list(range(n + 1))
                self.component_size = [1] * (n + 1)
                self.components = n
            
            def find_representative(self, x):
                if self.representative[x] == x:
                    return x
                self.representative[x] = self.find_representative(self.representative[x])
                return self.representative[x]
            
            def perform_union(self, x, y):
                x = self.find_representative(x)
                y = self.find_representative(y)
                
                if x == y:
                    return 0
                
                if self.component_size[x] > self.component_size[y]:
                    self.component_size[x] += self.component_size[y]
                    self.representative[y] = x
                else:
                    self.component_size[y] += self.component_size[x]
                    self.representative[x] = y
                
                self.components -= 1
                return 1
            
            def is_connected(self):
                return self.components == 1
        
        # Main function logic
        alice = UnionFind(n)
        bob = UnionFind(n)
        
        edges_required = 0
        
        for edge in edges:
            if edge[0] == 3:
                edges_required += (alice.perform_union(edge[1], edge[2]) | bob.perform_union(edge[1], edge[2]))
        
        for edge in edges:
            if edge[0] == 2:
                edges_required += bob.perform_union(edge[1], edge[2])
            elif edge[0] == 1:
                edges_required += alice.perform_union(edge[1], edge[2])
        
        if alice.is_connected() and bob.is_connected():
            return len(edges) - edges_required
        
        return -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #https://www.youtube.com/watch?v=booGwg5wYm4
        # Disjoint Set - union find data structure
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #------------------------------------------------------------
        # 1st make a hashmap with all edges note the types 
        # eliminate edages that have type 3 and other type
        
        # 2. simplify, divide conquer? make one adjacecy list for 
        #    Alice and  another for  Bob
        
        
        # have to verify if all nodes are coencted for alice and bob
        # ?like a Topological Sort Algorithm? Kruskals algorithm??
        # find loops?
        
        
        
        
        
        
        
        