class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
# opcion 1, lenta
#         cont = 0
#         i = 0
#         while  -1*(i-1)<=len(s) and s[i-1] == ' ':
#             i -= 1
             
#         while -1*(i-1)<=len(s) and  s[i-1] != ' ':
#             cont +=1
#             i -=1
#         return cont


# opcion 2, mas lenta pero elegante
#         return len(s.split()[-1])
        
        empezado_conteo = False
        conteo = 0 
        for letter in s[::-1]:
            if not empezado_conteo:
                if letter != ' ':
                    conteo = 1
                    empezado_conteo = True
            else:
                if letter != ' ':
                    conteo += 1
                else:
                    break
        return conteo
        