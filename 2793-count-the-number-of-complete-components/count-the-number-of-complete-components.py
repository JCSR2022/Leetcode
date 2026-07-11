class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:


        # adj = defaultdict(set)
        # for a, b in edges:
        #     adj[a].add(b)
        #     adj[b].add(a)

        # def dfs(node):
        #     seen.add(node)
        #     component.append(node)
        #     for nei in adj[node]:
        #         if not nei in seen: dfs(nei)


        # res = 0
        # seen = set()
        # for node in range(n):
        #     if not node in seen:
        #         component = []
        #         dfs (node)
        #         c = len(component)

        #     valid = True
        #     for i in range(c):
        #         for j in range(i + 1, c):
        #             if not component[i] in adj[component[j]]:
        #                 valid = False
        #                 break
        #         if not valid: 
        #             break
            
        #     if valid: 
        #         res += 1

        # return res

#------------------------------------------------------


        A = defaultdict(list)
        for u, v in edges:
            A[u].append(v)
            A[v].append(u)

        vis, res = [False] * n, 0
        for i, state in enumerate(vis):
            if not state:
                E = V = 0

                def dfs(x):
                    nonlocal V, E
                    V += 1
                    E += len(A[x])
                    vis[x] = True

                    for state in A[x]:
                        if not vis[state]:
                            dfs(state)

                dfs(i)
                res += E == V * (V - 1)

        return res
