class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        #aproach hash

        hash_nums = defaultdict(set)
        for i,n in enumerate(nums):
            hash_nums[n].add(i)

        ans = [0]*len(nums)
        for i,n in enumerate(nums):
            ans[i] = sum( abs(i-j) for j in hash_nums[n] if i !=j)

        return ans 





        