class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        p = n-1
        ans = -1
        while p > n//2:
            suma1 = p*(p+1)//2
            suma2 = sum([_ for _ in range(p,n+1)])

            if suma1 == suma2:
                ans = p
                break
            p -=1
            
        return ans
        