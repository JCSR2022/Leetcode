class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        unionFind = [ i for i in range(n)]
        for i in range(1,n):
            if abs(nums[i] - nums[i-1]) <= maxDiff:
                unionFind[i] = unionFind[i-1]
                
        
        return [ unionFind[qi]==unionFind[qv] for qi,qv in queries ]
