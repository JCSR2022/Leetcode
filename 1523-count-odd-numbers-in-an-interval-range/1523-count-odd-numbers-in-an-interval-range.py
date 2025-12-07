class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        s = high-low
        
        return s//2+s%2 if low%2 == 0 else s//2+1 
        
    