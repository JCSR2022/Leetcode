class UnionFind:
    def __init__(self, n):
        self.arr = [i for i in range(n)]
        self.rank = [0] * n


    def find(self,x):
        if not self.arr[x] == x:
            self.arr[x] = self.find(self.arr[x])
        return self.arr[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return
        
        if self.rank[px] < self.rank[py]:
            self.arr[px] = py
        elif self.rank[px] > self.rank[py]:
            self.arr[py] = px
        else:
            self.arr[py] = px
            self.rank[px] += 1


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        #unionfind on allowedSwaps

        #{0,1} {2,3} {}
        # indexs 0,1 => {1,2}  {1,2} => {} 0//2 = 0
        # indexs 2,3 => {4,5}  {3,4} => {3,5}  2//2 = 1

        #{}
        #indexs 0,1,2,3 ={1,2,3,4} {1,2,3,4} 

        #{0,4,2,1,3}

        n = len(source)
        uf = UnionFind(n)

        for a,b in allowedSwaps:
            uf.union(a,b)
        
        groups = defaultdict(lambda:defaultdict(int))
        for i in range(n):
            groups[uf.find(i)][source[i]] +=1


        ans = 0
        for i in range(n):
            g = groups[uf.find(i)]
            t = target[i]
            if g[t] > 0:
                g[t] -=1
            else:
                ans +=1
        return ans







        