class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:


        #brute force as allways , as teh only thing you can do

        ans = 0
        for num in nums:
            divisors = set()
            for i in range(1,num+1):
                if num%i == 0:
                    divisors.add(i)
                if len(divisors) > 4:
                    break
            if len(divisors) == 4:
                ans += sum(divisors)

        return ans





#----------------------------------------------------------------------------------------------        
        # def findPrimes(num):
        #     primes = [True for _ in range(num+1)]
        #     primes[0] = False
        #     primes[1] = False
        #     for i in range(2, num+1):
        #         if primes[i]:
        #             for j in range(i*i, num+1, i):
        #                 primes[j] = False
        #     return set(i for i in range(num+1) if primes[i])

        # primes = findPrimes(max(nums))

        # ans = 0
        # for num in nums:
        #     divisors = defaultdict(int)
        #     divisors[1] = 1
        #     for prime in primes:
        #         while num%prime == 0:
        #             divisors[prime] +=1 
        #             num /= prime 
        #         if num == 1: break
        #     print(dict(divisors))

        # return 15


        #nooooooooo imbecil
#----------------------------------------------------------------------------------------------



            
