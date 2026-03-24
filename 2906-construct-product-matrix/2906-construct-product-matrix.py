class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        #this should works for python because no need for mod only at the end
        #  O(2*n*m)

        mod = 12345

        n = len(grid)
        m = len(grid[0])

        mult = 1
        for row in grid:
            for val in row:
                mult *=val


        p = [ [0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m): 
                p[i][j] += (mult//grid[i][j])%mod
        
        return p
                
#Time Limit Exceeded?
#---------------------------------------------------------------------

        #Mantener números pequeños con % mod es la clave real de velocidad
        #mult *= val, hace que mult crezca enormemente.Después de multiplicar muchos números:
        # mult puede tener cientos o miles de bits
        # Cada nueva multiplicación es más cara
        # La división mult // grid[i][j] es muy costosa




        mod = 12345

        n, m = len(grid), len(grid[0])

        # Flatten grid
        flat = [grid[i][j] for i in range(n) for j in range(m)]
        size = len(flat)

        # Prefix
        prefix = [1] * size
        for i in range(1, size):
            # Después de cada operación se hace % mod
            prefix[i] = (prefix[i-1] * flat[i-1]) % mod

        # Suffix
        suffix = [1] * size
        for i in range(size-2, -1, -1):
            #Entonces los números nunca crecen más allá de mod (~12345)
            suffix[i] = (suffix[i+1] * flat[i+1]) % mod

        # print(flat)
        # print(prefix)
        # print(suffix)

        # Build result
        p = [[0]*m for _ in range(n)]
        for i in range(size):
            val = (prefix[i] * suffix[i]) % mod
            r, c = divmod(i, m)
            p[r][c] = val

        return p