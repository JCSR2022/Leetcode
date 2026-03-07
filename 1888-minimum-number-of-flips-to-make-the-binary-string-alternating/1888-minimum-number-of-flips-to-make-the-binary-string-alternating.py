class Solution:
    def minFlips(self, s: str) -> int:

        
        """
        Type-1 does not change Type-2 requeriments
        111000   2 -> 101000 -> 101010
        110001   2 -> 010001 -> 010101
        100011   2 -> 100010 -> 101010
        000111   2 -> 000101 -> 010101 
        001110   2 -> 001010 -> 101010
        """
        
        #Again 
        size = len(s)
        ones  = [1 if i%2==0 else 0 for i in range(size) ]
        ceros = [0 if i%2==0 else 1 for i in range(size) ]

        cnt_ones = 0
        cnt_ceros = 0
        for i in range(size):
            n = int(s[i])
            cnt_ones  += n != ones[i]
            cnt_ceros += n != ceros[i]

        return min(cnt_ceros,cnt_ones)
