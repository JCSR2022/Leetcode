from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return  False
        
#         def contar(entrada):
#             dicc_cuenta = {}
#             for elem in entrada:
#                 if elem in dicc_cuenta:
#                     dicc_cuenta[elem] += 1
#                 else:
#                     dicc_cuenta[elem] = 1
#             return dicc_cuenta

#         dicc_letras_word1 = contar(word1)       
#         dicc_letras_word2 = contar(word2)  
        
#         #condicion 1
#         letras_word1 = set(dicc_letras_word1.keys())
#         letras_word2 = set(dicc_letras_word2.keys())
#         if set(letras_word1) != set(letras_word2):
#             return False
        
#         #condicion 2
#         frecuencias_word1 = contar(list(dicc_letras_word1.values()))
#         frecuencias_word2 = contar(list(dicc_letras_word2.values()))
#         if frecuencias_word1 != frecuencias_word2:
#             return False   
            
#         return True   
            
        dicc_letras_word1 = Counter(word1)       
        dicc_letras_word2 = Counter(word2)  
        
        #condicion 1
        letras_word1 = set(dicc_letras_word1.keys())
        letras_word2 = set(dicc_letras_word2.keys())
        if set(letras_word1) != set(letras_word2):
            return False
        
        #condicion 2
        frecuencias_word1 = Counter(list(dicc_letras_word1.values()))
        frecuencias_word2 = Counter(list(dicc_letras_word2.values()))
        if frecuencias_word1 != frecuencias_word2:
            return False   
            
        return True      
    
    
            
            