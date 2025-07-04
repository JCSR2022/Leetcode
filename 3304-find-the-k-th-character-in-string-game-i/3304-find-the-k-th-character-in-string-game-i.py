class Solution:
    def kthCharacter(self, k: int) -> str:
        
        #brute force
        def change_ch(word):
            ans = []
            for ch in word:
                ans.append(chr(((ord(ch)-97)+1)%26+97) ) 
            return "".join(ans)

        ans = 'a'
        while len(ans) < k:
            ans += change_ch(ans)

        #print(ans)
        return ans[k-1]