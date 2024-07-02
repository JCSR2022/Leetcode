class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        #hashmaps
        
        hash1 = defaultdict(int)
        hash2 = defaultdict(int)
        
        for n in nums1: hash1[n] += 1
        for n in nums2: hash2[n] += 1
        
        ans = []
        for n in hash1.keys():
            if n in hash2:
                ans += [n]*min(hash1[n],hash2[n])
        
        return ans