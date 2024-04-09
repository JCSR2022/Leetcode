from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # firs aproach:
        nums = [i for i in range(1, n + 1)]
        print(nums)
        return list(combinations(nums, k))
