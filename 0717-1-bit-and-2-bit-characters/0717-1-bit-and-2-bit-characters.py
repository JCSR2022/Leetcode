class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        #brute force O(n)
        # from the begining if 2 digits are 10,11 is second caracter
        # if found 00,01, mot be first caracter 0[0xxx] or 0[1xxx]

        size = len(bits)
        if size == 1:
            return True

        i = 0
        while True:
            #print(i,bits[i:i+1])
            if i+1 < size and (bits[i],bits[i+1]) in [(1,0),(1,1)]:
                i += 2
                if i == size:
                    return False
            else:
                i += 1
                if i == size:
                    return True
