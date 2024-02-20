class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # brute force
        lista = [ _ for _ in range(len(nums)+1)][::-1]
        for num in nums:
            lista.remove(num)
        return lista[0]
