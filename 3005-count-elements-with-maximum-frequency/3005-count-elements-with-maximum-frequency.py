from collections import defaultdict

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

#         hashMap = defaultdict(int)

#         for n in nums:
#             hashMap[n] += 1
            
#         maxFrecuency = max(hashMap.values())
#         count_maxFrecuency = 0
        
#         for frec in hashMap.values():
#             if frec == maxFrecuency:
#                 count_maxFrecuency += 1
        
#         return count_maxFrecuency*maxFrecuency

        freq=[0]*101
        maxF=0
        for x in nums:
            freq[x]+=1
            maxF=max(maxF, freq[x])
        ans=0
        for f in freq:
            if f==maxF:
                ans+=f
        return ans
                