class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        cnt_open = 0
        ans = 0
        for ch in s:
            if ch == '(':
                cnt_open +=1
            else:
                if cnt_open > 0:
                    cnt_open -= 1
                else:
                    ans += 1
                    
        return ans + cnt_open