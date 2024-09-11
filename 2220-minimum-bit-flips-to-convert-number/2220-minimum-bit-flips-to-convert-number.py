class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        resultado = start ^  goal
        return bin(resultado).count('1')