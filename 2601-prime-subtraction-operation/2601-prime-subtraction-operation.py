class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        
        primes = []
        def is_prime(n):
            if n in primes:
                return True
            else:
                for x in range(2,int(math.sqrt(n))+1):
                    if n%x == 0:
                        return False
                primes.append(n)
                return True
            
            
        prev = 0
        for n in nums:
            upper = n - prev
            
            largest = 0 
            for i in reversed(range(2,upper)):
                if is_prime(i):
                    largest = i
                    break
            
            if n - largest <= prev:
                return False
            
            prev = n - largest
            
        return True
        