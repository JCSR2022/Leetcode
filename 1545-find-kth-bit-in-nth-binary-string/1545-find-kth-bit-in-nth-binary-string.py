class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def reverse(s):
            return s[::-1]

        def invert(s):
            return ''.join('1' if c == '0' else '0' for c in s)
        
        def locura(s:str):
            return s + "1" + reverse(invert(s))
        
        
        s = "0"
        for _ in range(n-1):
            s = locura(s)
            
       # print(s)
        return s[k-1]