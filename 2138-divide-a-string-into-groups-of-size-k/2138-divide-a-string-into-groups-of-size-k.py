class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        N = len(s)
        ans = []
        for i in range(0,N,k):
            ans.append(s[i:i+k])
        
        last = [fill]*k
        for j,ch in enumerate(ans[-1]):
            last[j] = ch
        ans[-1] = "".join(last)
        
        return ans