class Solution:
    def minimumPushes(self, word: str) -> int:

        chars = Counter(word)
        #print(dict(chars), sorted(chars.values(),reverse=True))
        ans = 0
        for i,cnt in enumerate(sorted(chars.values(),reverse=True)):
           ans += (i//8+1)*cnt

        return ans
        