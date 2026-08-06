class Solution:
    def smallestNumber(self, n: int, t: int) -> int:


        def digProd(x):
            digitsProduct = 1
            while x>0:
                digitsProduct *= x%10
                x //=10
            return digitsProduct



        while digProd(n)%t != 0:
            n +=1
        
        return n
            
