class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        #bin(10**6+1)[2:],len(bin(10**6+1)[2:])
        primes = {2,3,5,7,11,13,17}

        ans = 0
        for num in range(left,right+1):
            if bin(num)[2:].count('1') in primes:
                ans +=1

        return ans
            
        