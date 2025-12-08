class Solution:
    def countTriples(self, n: int) -> int:

        #n = 250, so can use realy brute force n**2

        # ans = 0
        # for a in range(1,n):
        #     for b in range(1,n):
        #         if a**2+b**2 > n**2:
        #             break
        #         for c in range(1,n+1):  
        #             if a**2+b**2 == c**2:
        #                 ans +=1 
        # return ans

#Time Limit Exceeded
#--------------------------------------------------------------------------
        ans = 0
        for a in range(1,n):
            for b in range(a,n):        
                if a**2+b**2 <= n**2:
                    if math.sqrt(a**2+b**2) -int(math.sqrt(a**2+b**2)) == 0:
                        #print( f"{a**2} + {b**2} = {a**2+b**2}  ")
                        ans +=2
                else:
                    break
        return ans
                


