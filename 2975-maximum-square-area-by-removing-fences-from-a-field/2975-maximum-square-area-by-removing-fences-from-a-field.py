class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        
        mod = 10**9+7

        hFences = [1]+sorted(hFences)+[m]
        h_gaps = set()
        for i in range(len(hFences)):
            for j in range(i+1,len(hFences)):
                h_gaps.add(hFences[j]-hFences[i])
        

        vFences = [1]+sorted(vFences)+[n]
        v_gaps = set()
        for i in range(len(vFences)):
            for j in range(i+1,len(vFences)):
                v_gaps.add(vFences[j]-vFences[i])

        squares = [ gap for gap in h_gaps if gap in v_gaps]

        return (max(squares)**2)%mod  if squares else -1
        