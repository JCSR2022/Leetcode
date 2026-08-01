class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        #brute force

        # my_memory = {}
        # def dfs(i,j,p1_score,p2_score,turn):
            
        #     if (i,j,p1_score,p2_score,turn) in my_memory:
        #         return my_memory[(i,j,p1_score,p2_score,turn)]

        #     if i==j:
        #         return  p1_score >= p2_score

        #     if turn == 1:
        #         opc1 = dfs(i+1,j,p1_score+nums[i],p2_score,2)
        #         opc2 = dfs(i,j-1,p1_score+nums[j],p2_score,2)
        #     else:
        #         opc1 = dfs(i+1,j,p1_score,p2_score+nums[i],1)
        #         opc2 = dfs(i,j-1,p1_score,p2_score+nums[j],1)
            
        #     my_memory[(i,j,p1_score,p2_score,turn)] = opc1 | opc2

        #     return my_memory[(i,j,p1_score,p2_score,turn)] 

        # size = len(nums)
        # return dfs(0,size-1,0,0,1)
            
#maldito imbecil ni siqueira la brute force!!???
#-----------------------------------            
        memo = {}
        
        # dfs devuelve la máxima diferencia (Puntos Propios - Puntos Rival)
        # que el jugador actual puede asegurar desde el subarreglo nums[i...j]
        def dfs(i, j):
            if i == j:
                return nums[i]
            if (i, j) in memo:
                return memo[(i, j)]
            
            # El jugador actual elige el inicio o el final,
            # y se le resta lo que el rival obtenga óptimamente después.
            elegir_izquierda = nums[i] - dfs(i + 1, j)
            elegir_derecha = nums[j] - dfs(i, j - 1)
            
            # Al ser óptimo, el jugador actual maximiza su ventaja
            memo[(i, j)] = max(elegir_izquierda, elegir_derecha)
            return memo[(i, j)]
        
        # Si la diferencia a favor del Jugador 1 es >= 0, él gana
        return dfs(0, len(nums) - 1) >= 0



