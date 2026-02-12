class Solution:
    def longestBalanced(self, s: str) -> int:

        #brute force

        ans = 0
        for start in range(len(s)):
            count = defaultdict(int)
            for end in range(start,len(s)):
                count[s[end]] +=1
                if len(set([v for v in count.values()])) == 1:
                    ans = max(ans,end-start+1)

        return ans



        