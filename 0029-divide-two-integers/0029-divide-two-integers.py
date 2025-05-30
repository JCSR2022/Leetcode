class Solution:
    def divide(self, dividend: int, divisor: int) -> int:


        if dividend == divisor:
            return 1
        if dividend == -2**31 and divisor == -1:
            return (2**31) - 1 
        
        if divisor == 1:
            return dividend
        
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        n, d = abs(dividend), abs(divisor)
        ans = 0

        while n >= d:
            p = 0
            while n >= (d << p):
                p += 1
            
            p -= 1
            n -= (d << p)
            ans += (1 << p)

        return min(max(sign * ans, -2**31), 2**31 - 1)






#--------------------------------------------------------------
#simplemente no entiendo esta maldita mierda!!!!!!!!!!!!!!!!!        
        # positive = False
        # if  dividend > 0 and  divisor > 0:
        #     positive = True
        # elif dividend < 0 and  divisor < 0:
        #     positive = True

        # if  dividend < 0:
        #     dividend = -dividend
        # if divisor < 0 :
        #     divisor  = -divisor 

        # if divisor == 1 and dividend > 1:
        #     return dividend-1 if positive else -(dividend-1)

        # if dividend == divisor :
        #     return 1 if positive else -1

        # if dividend < divisor or dividend == 0:
        #     return 0
        

        # num = divisor
        # ans = 0
        # while num <= dividend:
        #     num += divisor
        #     ans +=1

        # return ans if positive else -ans
         
