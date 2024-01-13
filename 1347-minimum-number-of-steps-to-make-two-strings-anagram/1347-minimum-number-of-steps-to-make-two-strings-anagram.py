class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        def constDiccLetters(string_input):
            dicc = {}
            for letter in  string_input:
                if letter not in dicc:
                    dicc[letter] = 1
                else:
                    dicc[letter] += 1
            return dicc
        
        dicc_s = constDiccLetters(s)
        
        
        steps = 0
        
        dicc_t = {}
        for letter in t:
            if letter not in dicc_s:
                steps +=1
            else:
                if letter not in dicc_t:
                    dicc_t[letter] = 1
                else:
                    if dicc_t[letter] < dicc_s[letter]:
                        dicc_t[letter] += 1
                    else:
                        steps +=1
                        
        return steps
                     
        
        
        