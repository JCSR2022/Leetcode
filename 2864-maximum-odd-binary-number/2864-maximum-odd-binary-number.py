class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        ceros = 0
        ones = 0
        
        for c in s:
            if c == '1':
                ones +=1
            else:
                ceros +=1
               
        if ones == 1:
            return "0"*ceros+"1"
        else:
            return "1"*(ones-1) +"0"*ceros+"1"
        