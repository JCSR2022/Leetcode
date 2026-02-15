class Solution:
    def addBinary(self, a: str, b: str) -> str:

        ans = []
        carry = 0

        max_len = max(len(a),len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        for i in range(max_len-1,-1,-1):
            curr = int(a[i])+int(b[i])+carry
            carry = 0
            if curr == 0:
                ans.append('0')
            elif curr == 1:
                ans.append('1')
            elif curr == 2:
                ans.append('0')
                carry = 1
            elif curr == 3:
                ans.append('1')
                carry = 1
                
        if carry ==1:
            ans.append('1')

        return "".join(ans[::-1])

            





#-------------------------------------------------------------
        # dec_a = int(a, 2)
        # dec_b = int(b, 2)
        
        # return bin(dec_a+dec_b)[2:]
        