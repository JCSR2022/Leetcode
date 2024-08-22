class Solution:
    def findComplement(self, num: int) -> int:
        
        num_bin = bin(num)[2:]
        l = len(num_bin)
        ans = 0
        for i,b in enumerate(num_bin):
            if b == '0':
                ans += 2**(l-i-1)
                
        return ans