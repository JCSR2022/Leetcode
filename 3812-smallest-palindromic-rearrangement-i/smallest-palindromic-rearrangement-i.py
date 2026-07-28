class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
        # base = ord('a')

        # hash_ch = [0]*26
        # for ch in s:
        #     hash_ch[ord(ch) - base] +=1
        
        # ans = "" 
        # is_odd = ""
        # for i in range(26):
        
        #     if hash_ch[i]%2 != 0:
        #         is_odd = chr(i + base)
        #         hash_ch[i] -= 1

        #     ans += chr(i + base)*(hash_ch[i]//2)

        # ans += is_odd + ans[::-1]

        # return ans
#---------------------------------------------------

        counts = sorted(Counter(s).items())
        half = "".join(c * (k // 2) for c, k in counts)
        mid  = "".join(c * (k % 2)  for c, k in counts)
        return half + mid + half[::-1]