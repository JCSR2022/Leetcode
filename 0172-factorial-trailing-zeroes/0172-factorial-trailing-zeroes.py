class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        #brute force
        #dosent work on big numbers
        
#         def factorial(n):
#             ans = 1
#             for i in range(1,n+1):
#                 # print(i,ans)
#                 ans *= i
                
#             return ans
        
#         fact = str(factorial(n))[::-1]
#         print(fact[::-1])
        
#         zeroes = 0
#         i = 0
#         while i <len(fact) and fact[i] == '0' :
#             i += 1
#             zeroes += 1
        
#         return zeroes

    
    

        # Matematical aproach:
        # numb of ceros is the number of 5 in n!
        # example : 6! = 6*5*4*3*2*1 = 720       1
        #           10! = 3628800                2
        #           15! = 1307674368000          3
        #           20! = 2432902008176640000    4
        #           25! = 15511210043330985984000000  note here 25 = 5*5...... 6
        #           30! = 265252859812191058636308480000000...                 7
        
        
#         first try:
#         count = 0
#         num = [ i for i in range(1,n+1) if i%5 == 0]
#         #print(num)
#         for elem in num:
#             count += 1
#             while (elem//5)%5 == 0:
#                 count += 1
#                 elem = elem//5
                
#         return count
        
        count = 0
        
        while n > 0:
            #print(n,[ i for i in range(1,n+1) if i%5 == 0],n//5,count)
            count += n//5
            n //= 5
            
        return count

        




        
        