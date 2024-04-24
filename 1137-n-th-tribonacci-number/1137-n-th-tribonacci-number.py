class Solution:
    def tribonacci(self, n: int) -> int:
        
        
        hash_result = {}
        
        def cal_3fib(n):
            if n == 2:
                return 1
            if n == 1:
                return 1
            if n == 0:
                return 0
            
            if n in hash_result:
                return hash_result[n]
            else:
                ans = cal_3fib(n-1) + cal_3fib(n-2) + cal_3fib(n-3) 
                hash_result[n] = ans
                return ans

        
        return cal_3fib(n)
        
        