class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        # approach: find num of age on nodes, order and give bigest valu to more_ages_nodes
        
        
        edges = defaultdict(int)
        for edge in roads:
            edges[edge[0]] +=1
            edges[edge[1]] +=1
        #print(edges)
        
        sorted_edges = dict(sorted(edges.items(), key=lambda item: item[1], reverse=True))
        #print(sorted_edges)
        
        nodes_val = defaultdict(int)
        for val,node in enumerate(sorted_edges.keys()):
            nodes_val[node] = n-val
        #print( nodes_val)
        
        ans = 0
        for n1,n2 in roads:
            ans += nodes_val[n1] + nodes_val[n2]
        
        return ans