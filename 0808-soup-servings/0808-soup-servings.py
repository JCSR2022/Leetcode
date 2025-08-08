class Solution:
    def soupServings(self, n: int) -> float:

        #math solution is using Expected values
        #prog sol is using dfs


        # def dfs(cnt,A,B):
        #     print(" "*cnt,cnt,".",A,B)
        #     #return [cnt_A,cnt_AB,cnt_B]

        #     if A <=0 and B <= 0:
        #         return [0,1,0]
        #     if A <= 0:
        #         return [1,0,0]            
        #     if B <= 0:
        #         return [0,0,1]

        #     pos1 = dfs(cnt+1,A-100,B)
        #     pos2 = dfs(cnt+1,A-75,B-25)
        #     pos3 = dfs(cnt+1,A-50,B-50)
        #     pos4 = dfs(cnt+1,A-25,B-75)
            
        #     print(" "*cnt,cnt,(A-100,B),".pos1:",pos1)
        #     print(" "*cnt,cnt,(A-75,B-25),".pos2:",pos2)
        #     print(" "*cnt,cnt,(A-50,B-50),".pos3:",pos3)
        #     print(" "*cnt,cnt,(A-25,B-75),".pos4:",pos4)

        #     ans = [ x+y+z+w for x,y,z,w in zip(pos1,pos2,pos3,pos4)]

        #     print(" "*cnt,cnt,".ans:",ans)

        #     return ans

        # ans = dfs(0,n,n)
        # print(f"ans = ({ans[0]} + {ans[1]/2})/ {sum(ans)}")
        # return  (ans[0] + ans[1]/2)/sum(ans) 

        """no funciona:
        No todos los caminos tienen la misma probabilidad
        El código cuenta los caminos, pero lo que se necesita 
        es la probabilidad total, no la frecuencia.

        Por ejemplo:
        Cada llamada recursiva representa una decisión 
        entre 4 posibles operaciones, cada una con probabilidad 0.25.

        Entonces:

        Un camino de profundidad 1 tiene peso 0.25
        Un camino de profundidad 2 tiene peso 0.25 × 0.25 = 0.0625
        Y así sucesivamente.

        Pero el código suma todos los caminos como si 
        todos valieran lo mismo (peso uniforme), 
        lo cual distorsiona completamente la probabilidad real.
        """

#--------------------------------------------------------------------


        @lru_cache(None)
        def dfs(cnt, A, B):
            #print(" " * cnt, f"{cnt}.({A},{B})")

            # Caso base: A y B vacíos a la vez
            if A <= 0 and B <= 0:
                return 0.5
            # Caso base: solo A vacío
            if A <= 0:
                return 1.0
            # Caso base: solo B vacío
            if B <= 0:
                return 0.0

            # Recurre con cada opción, ponderando con 0.25
            prob1 = dfs(cnt + 1, A - 100, B)
            prob2 = dfs(cnt + 1, A - 75, B - 25)
            prob3 = dfs(cnt + 1, A - 50, B - 50)
            prob4 = dfs(cnt + 1, A - 25, B - 75)

            result = 0.25 * (prob1 + prob2 + prob3 + prob4)

            #print(" " * cnt, f"Result({A},{B}) = {result}")
            return result

        return dfs(0, n, n)