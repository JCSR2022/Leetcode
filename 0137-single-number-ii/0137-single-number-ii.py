class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ones = 0
        twos = 0

        for num in nums:
          ones ^= (num & ~twos)
          twos ^= (num & ~ones)

        return ones
        
        
#         hashMap = defaultdict(int)
        
#         for n in nums:
#             hashMap[n] += 1
        
#         for k,v in hashMap.items():
#             if v == 1:
#                 return k
            
#         return -1
        
        