class Solution:
    def hammingWeight(self, n: int) -> int:
        
        res = 0
        while n:
            n &= (n-1)
            res +=1
        
        return res
        
        # s=int(n) 
        # b=str(bin(s)) 
        # return b.count("1")
        
        #return n.bit_count()
        
        #print(type(n))
        #return bin(n)[2:].count('1')
        