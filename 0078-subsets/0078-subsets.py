class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums)+1):
            ans += [list(x) for x in itertools.combinations(nums, i)]  
            
        return ans