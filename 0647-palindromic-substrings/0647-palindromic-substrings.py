class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = []
        for i in range(len(s)):
            for j in range(i):
                if s[j:i+1] == s[j:i+1][::-1]:
                    ans.append(s[j:i+1])
        L_ans = len(list(s)) + len(ans)
        
        return L_ans
        