class Solution:
    def fractionAddition(self, expression: str) -> str:
        
        #divide:
        #  1.create a function to read all num, save it as [[num1,den1],[num2,den2]..]
        #  2 crete a function that add all num and return [ans_num,ans_den]
        #  3. present result
        
        import re
        def readExp(exp:str):
            # Expresión regular para capturar numeradores y denominadores
            split_both = re.findall(r'([+-]?\d+)(?:/(\d+))?', exp)
            
            # Convertir a la forma deseada (numerador, denominador)
            result = []
            for num, denom in split_both:
                result.append((int(num),int(denom) if denom else 1))
            
            return result
        
        
        #from math import gcd
        from functools import reduce
        def suma_fracciones(fracciones):
            # Función para sumar dos fracciones (num1/den1) + (num2/den2)
            def suma_dos_fracciones(frac1, frac2):
                num1, den1 = frac1
                num2, den2 = frac2
                num = num1 * den2 + num2 * den1
                den = den1 * den2
                return (num, den)
            
            # Implementación del algoritmo de Euclides para encontrar el MCD
            def mcd(a, b):
                while b:
                    a, b = b, a % b
                return a

            # Suma todas las fracciones en la lista
            suma = reduce(suma_dos_fracciones, fracciones)

            # # Simplificar la fracción resultante
            # num, den = suma
            # divisor_comun = gcd(num, den)
            # return (num // divisor_comun, den // divisor_comun)
            
            # Simplificar la fracción resultante usando nuestro propio MCD
            num, den = suma
            divisor_comun = mcd(abs(num), abs(den))
            return (num // divisor_comun, den // divisor_comun)
        
        
        fracciones = readExp(expression)
        ans = suma_fracciones(fracciones)
            
        return str(ans[0])+"/"+str(ans[1]) 