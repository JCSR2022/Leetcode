class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        if n < 0:
            x **= -1
            n *= -1
        if n % 2 == 1:
            return x * self.myPow(x, n - 1)
        else:
            num = self.myPow(x, n // 2)
            return num * num        
        
#         if n > 0:
        
#             ans = 1
#             for _ in range(n):
#                 ans *= x
#             return ans
        
#         elif n == 0:
#             return 1
        
#         else:
#             n = -1*n
#             ans = 1
#             for _ in range(n):
#                 ans *= x
#             return 1/ans
        
        