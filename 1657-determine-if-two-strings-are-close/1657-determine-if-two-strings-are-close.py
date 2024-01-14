class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return  False
            
        def contar_letras(string_input):
            dicc_letras = {}
            for letra in string_input:
                if letra in dicc_letras:
                    dicc_letras[letra] += 1
                else:
                    dicc_letras[letra] = 1
            return dicc_letras

        dicc_letras_word1 = contar_letras(word1)       
        dicc_letras_word2 = contar_letras(word2)  
        
        letras_word1 = set(dicc_letras_word1.keys())
        letras_word2 = set(dicc_letras_word2.keys())
        
        cant_letras_word1 = list(dicc_letras_word1.values())
        cant_letras_word1.sort()
        
        cant_letras_word2 = list(dicc_letras_word2.values())
        cant_letras_word2.sort()
        
        cond1 = False
        cond2 = False
          
        #condicion 1
        if set(letras_word1) == set(letras_word2):
            cond1 = True
            
        #condicion 2
        if cant_letras_word1 == cant_letras_word2:
            cond2 = True
            
        return cond1 and cond2
        
        