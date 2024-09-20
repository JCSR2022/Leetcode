class Solution:
    
    def kmp(self, txt: str, patt: str) -> int:
        new_string = patt + '#' + txt
        pi = [0] * len(new_string)
        i = 1
        k = 0
        while i < len(new_string):
            if new_string[i] == new_string[k]:
                k += 1
                pi[i] = k
                i += 1
            else:
                if k > 0:
                    k = pi[k - 1]
                else:
                    pi[i] = 0
                    i += 1
        return pi[-1]
    
    def shortestPalindrome(self, s: str) -> str:
        #9.1 Algoritmo de coincidencia de cadenas KMP de Knuth-Morris-Pratt
        #https://www.youtube.com/watch?v=V5-7GzOfADQ
        
        
        count = self.kmp(s[::-1], s)
    
        return s[count:][::-1] + s



            
        