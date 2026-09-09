class Solution:

    pow1000 = [1000, 1000000, 1000000000, 1000000000000, 1000000000000000, 1000000000000000000]

    def countCommas(self, n: int) -> int:

        # comas = len(str(n))//3

        # print(comas)

        # print(n//(10**(3*comas)),n%(10**(3*comas)))

        # return 3
        
#esta semana estoy bruto!!!
#----------------------------------------------------------------------------
        # k = int(log10(n)) // 3        
        # return k * (n + 1) - (1000**(k + 1) - 1000) // 999

#--------------------------------------------------------
        k = 0
        for p in self.pow1000:
            k += n >= p
            
        return k * (n + 1) - (self.pow1000[k] - 1000) // 999