class Solution:
    def smallestSubsequence(self, s: str) -> str:

        # lastCh = {}
        # for i,ch in enumerate(s):
        #     lastCh[ch] = i

        # stack = []
        # for i,ch in enumerate(s):
        #     if not stack:
        #         stack.append(ch)
        #         continue

        #     while stack and ch < stack[-1] and lastCh[stack[-1]] > i:
        #         stack.pop()

        #     if ch not in stack:
        #         stack.append(ch)

        # return "".join(stack)


#eres un maldito imbecil incapaz y no lograras nada en la vida


        freq = Counter(s)
        seen = set()
        stack = []

        for c in s:
            freq[c] -= 1
            if c in seen: continue

            while stack and stack[-1] > c and freq[stack[-1]]:
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)

        return "".join(stack)

        