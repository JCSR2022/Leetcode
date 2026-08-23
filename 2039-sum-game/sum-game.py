class Solution:
    def sumGame(self, num: str) -> bool:
        #eres un maldito inutil de mierda 
 
        n = len(num)
        ans = 0.0

        def getExpectation(c: str) -> float:
            return 4.5 if c == '?' else int(c)

        for i in range(n // 2):
            ans += getExpectation(num[i])

        for i in range(n // 2, n):
            ans -= getExpectation(num[i])

        return ans != 0.0
