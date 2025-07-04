class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        #brute force:

        # def change_ch(word):
        #     ans = []
        #     for ch in word:
        #         ans.append(chr(((ord(ch)-97)+1)%26+97) ) 
        #     return "".join(ans)

        # ans = 'a'
        # for op in operations:
        #     if op:
        #         ans += change_ch(ans)
        #     else:
        #         ans +=ans
        # #print(ans)
        # return ans[k-1]

#of course Time Limit Exceeded
#---------------------------------------------------------
        #An-Wen Deng
        A=0
        for b in range((k-1).bit_length()):
            A|=(operations[b]<<b)
        return chr(97+((k-1) & A).bit_count()%26)


