class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:


        #BRUTE FORCE    

        def countWav(num):
            digits = [ int(n) for n in str(num)]
            size =  len(digits)
            if size < 3:
                return 0

            ans = 0
            for i in range(size-2):
                peak = digits[i+1] > digits[i]   and   digits[i+1] > digits[i+2] 
                valley = digits[i+1] < digits[i]   and   digits[i+1] < digits[i+2] 
                ans += peak or valley

            return ans 

        ans = 0
        for num in range(num1, num2+1):
            ans += countWav(num)

        return ans
        