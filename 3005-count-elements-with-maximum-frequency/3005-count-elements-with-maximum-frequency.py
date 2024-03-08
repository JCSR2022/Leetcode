from collections import defaultdict

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        hashMap = defaultdict(int)

        for n in nums:
            hashMap[n] += 1
            
        maxFrecuency = max(hashMap.values())
        count_maxFrecuency = 0
        
        for frec in hashMap.values():
            if frec == maxFrecuency:
                count_maxFrecuency += 1
        
        return count_maxFrecuency*maxFrecuency
                