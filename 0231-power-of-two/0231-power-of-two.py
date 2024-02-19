class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if bin(n)[0] == '-':
            return False
        
        
        # suma = 0
        # for elem in bin(n):
        #     if elem == '1':
        #         suma +=1
        #         if suma > 1:
        #             return False
        # return True
        
        
        
        return bin(n).count('1') == 1 
        
    
        