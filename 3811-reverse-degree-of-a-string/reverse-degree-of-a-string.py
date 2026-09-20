from string import ascii_lowercase


class Solution:
    def reverseDegree(self, s: str) -> int:



        value = { ch:(26-i)  for i,ch in enumerate(ascii_lowercase) }

        ans = 0
        for i,ch in enumerate(s):
            ans += value[ch]*(i+1)

        return ans       
        