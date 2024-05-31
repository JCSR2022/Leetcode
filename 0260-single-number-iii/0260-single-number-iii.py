class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        #brute force
        
        hashMap = defaultdict(int)
        
        for n in nums:
            hashMap[n] += 1
        
        ans = []
        
        for key,val in hashMap.items():
            if val == 1:
                ans.append(key)
        
        return ans