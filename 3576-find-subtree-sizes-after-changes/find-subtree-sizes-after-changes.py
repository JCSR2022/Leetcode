class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:

        #no se si hace falta pero
        adj = defaultdict(list)
        for i,n in enumerate(parent):
            adj[n].append(i)        
        print(dict(adj))
        last_seen = [-1]*26 #abcde..z



        def dfs(node):
            curr_ch = ord(s[node]) - ord('a')
            prev = last_seen[curr_ch]
            if prev != -1:
                parent[node] = prev
            last_seen[curr_ch] = node

            for nei in adj[node]:
                dfs(nei)
            last_seen[curr_ch] = prev
        dfs(0)

        adj2 = defaultdict(list)
        for i,n in enumerate(parent):
            adj2[n].append(i)

        @cache
        def dfs2(node):
            total = 1 
            for nei in adj2[node]: 
                total += dfs2(nei)
            return total

        res = [ dfs2(i) for i in range(len(parent))]

        return res








        
        return parent