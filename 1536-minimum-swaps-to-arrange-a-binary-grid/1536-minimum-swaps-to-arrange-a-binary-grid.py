class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:

        # n = len(grid)
        # #firs check if valid

        # arr = []
        # for row in grid:
        #     indx = 0
        #     for i in range(n):
        #         if row[i] == 1: indx = i
        #     arr.append(n-indx-1)

        # arr.sort(reverse=True)
        # for i in range(n):
        #     if arr[i]  < n-i-1:
        #         return -1

        # return 1

#----------------------------------------
        """

        Para que la cuadrícula sea válida, cada fila i debe tener al menos (n - i - 1) ceros finales. Porque:
        Fila 0 → necesita n-1 ceros
        Fila 1 → necesita n-2 ceros
        Fila 2 → necesita n-3 ceros
        ...
        Última fila → necesita 0 ceros
        Por lo tanto, en lugar de intercambiar toda la cuadrícula, hacemos lo siguiente:
        Contamos los ceros finales de cada fila.
        Intentamos colocar una fila válida en cada posición.
        Si hay una fila válida debajo, la subimos mediante intercambios adyacentes.
        Contamos los intercambios.
        Si ninguna fila cumple el requisito → devolvemos -1.
        """

        n = len(grid)
        zeros = []
        for row in grid:
            count = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            zeros.append(count)


        swaps = 0
        for i in range(n):
            needed = n - i - 1
            j = i
            while j < n and zeros[j] < needed:
                j += 1
            if j == n:
                return -1
            while j > i:
                zeros[j], zeros[j - 1] = zeros[j - 1], zeros[j]
                j -= 1
                swaps += 1

        return swaps
        