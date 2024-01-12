class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        def contarVocales(string_contar):
            lista_vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
            #CantVocales = { key:0 for key in lista_vocales}
            CantVocales = 0
            for letra in string_contar:
                if letra in lista_vocales:#CantVocales.keys():
                    #CantVocales[letra] +=1
                    CantVocales +=1
            return CantVocales
        
        mitad = len(s)//2
        
        return contarVocales(s[:mitad]) == contarVocales(s[mitad:])
        