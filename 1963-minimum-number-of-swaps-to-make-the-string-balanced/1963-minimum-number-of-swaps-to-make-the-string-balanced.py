class Solution:
    def minSwaps(self, s: str) -> int:
        
        cont = 0
        max_cont = 0
        for ch in s:
            if ch == ']': cont += 1
            else:cont -= 1
            max_cont = max(max_cont,cont)
            
        return (max_cont+1)//2
                