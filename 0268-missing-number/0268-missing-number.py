class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # # brute brute, brute force
        # lista = [ _ for _ in range(len(nums)+1)][::-1]
        # for num in nums:
        #     lista.remove(num)
        # return lista[0]
        n = len(nums)
        return n*(n+1)//2 - sum(nums)
