class Solution:
    def minOperations(self, s: str) -> int:
        
        # ans = 0
        # prev = s[0]
        # for digit in s[1:]:
        #     if digit == prev:
        #         ans +=1
        #         prev = '0' if  digit == '1' else '1'
        #     else:
        #         prev = digit
            
        # return ans 

#this is a pice of c@#%#%#@$%
#--------------------------------------------------------------

        #Aproach: s can be 0101010... or 101010101
        # so if beging with 0 count changes need, and if beging with 1 also count
        # ans is the min of boths

        size = len(s)
        ceros = [ 0 if i%2==0 else 1 for i in range(size)]
        ones  = [ 1 if i%2==0 else 0 for i in range(size)]
        count_0 = 0
        count_1 = 0
        for i in range(size):
            digit = int(s[i])
            count_0 += digit == ceros[i]
            count_1 += digit == ones[i]

        return min(count_0,count_1)
             

            













