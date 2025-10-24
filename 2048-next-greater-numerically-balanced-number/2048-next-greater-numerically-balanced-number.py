class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        for num in range(n+1,10**7+1):
            frec_map = Counter(str(num))
            if all( k == str(v) for  k,v in frec_map.items() ):
                return num
        