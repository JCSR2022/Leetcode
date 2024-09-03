class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        #import string

        # Obtener las letras del alfabeto inglés en minúsculas
        #letters = string.ascii_lowercase
        letters = "abcdefghijklmnopqrstuvwxyz"
        
        
        # string num
        num = int("".join([str(letters.index(x)+1) for x in s]))
            
            
        while k > 0:
            k -= 1
            num = sum([int(n) for n in str(num)])
        
        return num
    
    
    
    