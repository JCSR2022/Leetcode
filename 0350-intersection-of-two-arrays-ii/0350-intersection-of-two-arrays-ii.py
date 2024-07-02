class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        freq1 = {}
        freq2 = {}

        # Count the frequency of elements in nums1
        for num in nums1:
            freq1[num] = freq1.get(num, 0) + 1

        # Check if elements in nums2 are present in nums1 and add them to the result
        result = []
        for num in nums2:
            if num in freq1 and freq1[num] > 0:
                result.append(num)
                freq1[num] -= 1

        return result
        
        
        
        #hashmaps, O(n*m) where n is distinct num in nums1 and m the same for nums2
        
#         hash1 = defaultdict(int)
#         hash2 = defaultdict(int)
        
#         for n in nums1: hash1[n] += 1
#         for n in nums2: hash2[n] += 1
        
#         ans = []
#         for n in hash1.keys():
#             if n in hash2:
#                 ans += [n]*min(hash1[n],hash2[n])
        
#         return ans