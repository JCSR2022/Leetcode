class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
#         max_val = 0
#         nums.sort(reverse = True)
        
#         print(nums)
#         for i,n in enumerate(nums):
#             max_val += n
#             print(i,n,max_val)
#             if max_val >= target:
#                 return i+1
            
#         return 0

        # Calcula la suma total de la lista de números.
        summ = sum(nums)
        
        # Si la suma total es menor que el objetivo, no hay subarray que cumpla la condición.
        if summ < target:
            return 0

        # Inicializa los índices izquierdo (l) y derecho (r), 
        #   la suma actual y la longitud mínima.
        l, r = 0, 0
        sum_val = 0
        mini = float('inf')
        n = len(nums)

        # Realiza un bucle mientras el índice derecho sea menor que el tamaño de la lista.
        while r < n:
            # Si la suma actual es menor que el objetivo, 
            #   agrega el elemento en el índice derecho.
            if sum_val < target:
                sum_val += nums[r]
                r += 1
            # Si la suma actual es mayor o igual al objetivo, 
            # actualiza la longitud mínima y resta el elemento en el índice izquierdo.
            else:
                mini = min(mini, r - l)
                sum_val -= nums[l]
                l += 1

        # Realiza un bucle adicional para ajustar el índice izquierdo 
        #  mientras la suma aún cumple con la condición.
        while sum_val - nums[l] >= target:
            sum_val -= nums[l]
            l += 1

        # Actualiza la longitud mínima y devuelve el resultado.
        mini = min(mini, r - l)
        return mini
        
        
        