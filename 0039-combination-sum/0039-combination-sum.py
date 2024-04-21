class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        
        # brute force:
        
        ans = []
        
        def DescTree(i,current,total):
            #print(i,current,total,ans)
            if total == target:
                ans.append(current.copy())
                return
            
            if  total > target:
                return
            
            for n in candidates:
                current.append(n)
                DescTree(i+1,current,total+n)
                current.pop()
                
                
        candidates.sort()   
        DescTree(0,[],0)
        
        
        
        
        def filtrar_listas_sin_repetir(lista_de_listas):
            # Usar un conjunto para almacenar listas únicas
            # Ordenar la lista para que las listas con los mismos elementos, 
            # pero en diferente orden, sean consideradas iguales
            listas_unicas = set()
            resultado = []

            for lista in lista_de_listas:
                # Convertir la lista actual en una tupla para poderla agregar al conjunto
                lista_tupla = tuple(sorted(lista))  
                if lista_tupla not in listas_unicas:
                    # Agregar la lista al conjunto y al resultado si no está en el conjunto
                    listas_unicas.add(lista_tupla)
                    resultado.append(lista)

            return resultado
        
        ans = filtrar_listas_sin_repetir(ans)
        
        return ans
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # construir un decision tree , dfs.
        
#         res = []
        
#         def dfs(i,cur,total):
#             print(i,cur,total)
#             if total == target:
#                 res.append(cur.copy())
#                 return 
            
#             if i >= len(candidates) or total > target:
#                 return
            
#             cur.append(candidates[i])
#             dfs(i, cur, total+candidates[i])
#             cur.pop()
#             dfs(i+1, cur, total)
            
#         candidates.sort()    
#         dfs(0,[],0)
        
#         return res
            
            
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #aproch:
        # sort the candidates and try if target//candidates[0] == 0 
        # then try target// ((target//candidates[0] - 1)+candidates[1]) ==0
        
#         candidates.sort()
#         print(candidates)
        
#         for i in range(len(candidates)):
#             print(i,candidates[i], target//candidates[i],target%candidates[i])
        
#         return [[1]]
        