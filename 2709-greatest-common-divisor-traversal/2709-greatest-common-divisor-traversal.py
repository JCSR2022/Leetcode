#  I don't have the minum idea of how this work!!!   keep working hard!!!

class Solution:
    def getf(self, f, x):
        # Union-find: Find operation
        # Recursive function to find the root of the group to which x belongs
        return x if f[x] == x else self.getf(f, f[x])

    def merge(self, f, num, x, y):
        # Union-find: Merge operation
        # Merge two groups represented by x and y in the union-find data structure
        x = self.getf(f, x)
        y = self.getf(f, y)
        if x == y:
            return
        if num[x] < num[y]:
            x, y = y, x
        f[y] = x
        num[x] += num[y]

    def canTraverseAllPairs(self, nums):
        n = len(nums)
        if n == 1:
            return True

        # Initialize union-find data structure
        f = [i for i in range(n)]  # parent array
        num = [1] * n  # size of each group
        have = {}  # dictionary to store factors and their corresponding indices

        for i, x in enumerate(nums):
            if x == 1:
                return False

            for d in range(2, int(x**0.5) + 1):
                if x % d == 0:
                    if d in have:
                        self.merge(f, num, i, have[d])
                    else:
                        have[d] = i
                    while x % d == 0:
                        x //= d

            if x > 1:
                if x in have:
                    self.merge(f, num, i, have[x])
                else:
                    have[x] = i

        # Check if all indices belong to the same group
        return num[self.getf(f, 0)] == n
