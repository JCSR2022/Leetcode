class Solution:
    def isValid(self, s: str) -> bool:

        queue = []
        expected = {')':'(', '}':'{', ']':'['}

        for ch in s:
            if ch in {'(','{','['}:
                queue.append(ch)
            else:
                if not queue or queue[-1] != expected[ch]:
                    return False
                else:
                    queue.pop()

        return len(queue) == 0

        