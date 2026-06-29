class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:

        hash_pattern = Counter(patterns)

        ans = 0
        for patt,cnt in hash_pattern.items():
            if patt in word:
                ans += cnt

        return ans
        