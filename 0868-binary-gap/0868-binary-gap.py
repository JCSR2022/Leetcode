class Solution:
    def binaryGap(self, n: int) -> int:

        arr = [ ch =='1' for ch in bin(n)[2:]]

        for i in range(len(arr)):
            inc_l = i
            if arr[i]:break
        
        ans = 0
        l = inc_l
        for r in range(inc_l,len(arr)):
            if arr[r]:
                ans = max(ans,r-l)
                l = r

        return ans


        