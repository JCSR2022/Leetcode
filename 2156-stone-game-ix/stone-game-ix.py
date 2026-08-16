class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        "this has no sense, i am going to copy a solution and move forward"


        cnt = [0, 0, 0]

        for x in stones:
            cnt[x % 3] += 1

        # Alice can start with either remainder 1 or remainder 2.
        if cnt[1] == 0 and cnt[2] == 0:
            return False

        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0

        return abs(cnt[1] - cnt[2]) > 2


#vayanse a la maldita mierda