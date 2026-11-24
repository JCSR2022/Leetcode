class Solution:
    def maxLength(self, nums: List[int]) -> int:
         
        #fuerza bruta como tu imbecil, y ni siqueira pudiste, tuviste que usar ChtGPT!!!!
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i, n):  # Empieza en i (para subarreglos de tamaño 1)
                sub = nums[i:j+1]  # j+1 incluye el elemento en el índice j
                if math.prod(sub) == math.gcd(*sub) * math.lcm(*sub):
                    ans = max(ans, j - i + 1)
        return ans
