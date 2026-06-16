class Solution:
    def processStr(self, s: str) -> str:
        #brute force

        ans = []        
        for ch in s:
            if ch == '*':
                if ans: ans.pop()
            elif ch == "#":
                ans += ans
            elif ch == '%':
                ans = ans[::-1]
            else:
                ans.append(ch)

        return  "".join(ans)