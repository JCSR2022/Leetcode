class Solution:
    def compressedString(self, word: str) -> str:
        
        last_ch = word[0]
        cont = 0
        ans = ""
        for ch in word:
            if ch == last_ch and cont <9:
                cont +=1
            else:
                ans += str(cont)+last_ch
                last_ch = ch
                cont = 1
        
        ans += str(cont)+last_ch
        
        return ans
                
            
        