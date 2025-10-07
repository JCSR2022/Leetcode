from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        
        # n = len(rains)

        # lucklake = 0
        # for lake in rains:
        #     if lake != 0:
        #         lucklake = lake
        #         break 
        # ans = [lucklake]*n

        # ceros = SortedList()
        # lakes = {}
        
        # for i in range(n):
        #     if rains[i] > 0:
        #         ans[i] =-1
                
        #         if rains[i] in lakes:
        #             if ceros:
        #                 idx = ceros.bisect_left(lakes[rains[i]])
        #                 print(ceros, idx)
        #                 i_cero = ceros[idx]
        #                 if i_cero > lakes[rains[i]]:
        #                     ans[i_cero] = rains[i]
        #                     ceros.remove(i_cero)
                            
        #                 else:
        #                     return []
        #             else:
        #                 return []  
                
        #         lakes[rains[i]] = i

        #     else:
        #         ceros.add(i)


        # return ans

#maldito imbecil
#--------------------------------------------------------------------


        n = len(rains)
        uf = UnionFind(n + 1)
        map_lake = {}
        res = [1] * n

        for i, lake in enumerate(rains):
            if lake != 0:
                res[i] = -1
                uf.unite(i)
                
                if lake in map_lake:
                    prev = map_lake[lake]
                    dry = uf.find(prev + 1)
                    
                    if dry >= i:
                        return []

                    res[dry] = lake
                    uf.unite(dry)
                    map_lake[lake] = i
                else:
                    map_lake[lake] = i

        return res


class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size + 1))

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i: int):
        self.parent[i] = self.find(i + 1)