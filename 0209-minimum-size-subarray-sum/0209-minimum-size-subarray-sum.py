class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        #  Muy buena explicacion en https://www.youtube.com/watch?v=aYqYMIqZx5s


        summ = sum(nums)
        if summ < target:
            return 0

        
        r,l = 0,0
        min_leght = float("inf")
        sum_subarray = 0
        
#         while r < len(nums)-1:
#             print(nums[l:r],sum_subarray,min_leght)
#             if sum_subarray < target:
#                 r +=1
#                 sum_subarray += nums[r]
#             else:
#                 min_leght = min(min_leght,r-l)
#                 sum_subarray -= nums[l]
#                 l +=1
        
#         while sum_subarray- nums[l] > target:
#             print(nums[l:r],sum_subarray,min_leght)
#             sum_subarray -= nums[l]
#             l +=1
#             min_leght = min(min_leght,r-l)              
#         return  min_leght
            
                

        
        
        # Inicializa los índices izquierdo (l) y derecho (r), 
        #   la suma actual y la longitud mínima.
        l, r = 0, 0
        sum_val = 0
        mini = float('inf')
        n = len(nums)

        # Realiza un bucle mientras el índice derecho sea menor que el tamaño de la lista.
        while r < n:
            #print(l,r,nums[l:r],sum_val,mini)
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
            #print("x  ",l,r,nums[l:r],sum_val,mini,sum_val - nums[l])

        # Actualiza la longitud mínima y devuelve el resultado.
        mini = min(mini, r - l)
        #print(l,r,nums[l:r],sum_val,mini)
        return mini
        
        
        