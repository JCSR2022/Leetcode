class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        # codes = set([bin(num)[2:].zfill(k) for num in range(2**k)])

        # for code in codes:
        #     if not code in s:
        #         return False
        # return True
        
#Time Limit Exceeded
#----------------------------------------------------------------------

        code_size = 2**k
        
        codes = set( int(s[i:k+i],2) for  i in range(len(s)-k))

        return  len(codes) == code_size

# myset = set() 
# for i in range(0,len(letters)-k):
#   myset.add(int(letters[i:k+i],2))
#   print(i,letters[i:k+i],int(letters[i:k+i],2))
# print(myset)