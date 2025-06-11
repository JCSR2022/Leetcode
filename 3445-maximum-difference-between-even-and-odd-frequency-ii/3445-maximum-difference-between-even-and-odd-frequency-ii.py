class Solution:
    def maxDifference(self, s: str, k: int) -> int:


        #brute force, will not work for time O(n**2)

        N = len(s)
        ans = float("-inf")
        for i in range(N):
            for j in range(i+k-1,N):
                hash_count = Counter(s[i:j+1])
                max_odd  = max([float('-inf')]+[ n for n in hash_count.values() if n%2 != 0 ])
                min_even = min([float('inf')]+[ n for n in hash_count.values() if n%2 == 0 ]) 
                ans = max(ans,max_odd-min_even)
                #print(i,j,s[i:j+1],dict(hash_count),max_odd,min_even,ans)

        return ans

#-----------------------------------------------------------
        # sliding window?, can we be greedy?
        #want to max odd, min even
        #odd  111110301
        #     122331334
        #even 002222244

