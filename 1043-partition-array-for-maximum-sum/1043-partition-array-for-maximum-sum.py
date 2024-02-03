class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        D = [0] * len(arr)
        for idx in range(len(arr)):
            m = -float('inf')
            d = -float('inf')
            for jdx in range(0, min(k,idx+1)):
                m = max(arr[idx-jdx],m)
                d = max(d,m*(jdx+1) + D[idx-jdx -1])
            D[idx] = d
                #print(idx,jdx,m,D)
        return D[-1]
        
        