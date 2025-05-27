class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        #brute force

        # not_div = 0
        # div = 0
        # for i in range(1,n+1):
        #     if i%m == 0:
        #         div += i
        #     else:
        #         not_div +=i

        # return not_div-div
#---------------------------------------------------------------

        div = 0
        for i in range(1,n+1,m):
            div +=i

        print(n*(n+1)//2,n*(n+1)//2 - div ,div)

        #total = n*(n+1)//2
        #total  = div + not_div 
        #not_div  = total - div

        return  (n*(n+1)//2) - (2*div)      

        
