from collections import defaultdict

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        frec_dict = defaultdict(int)
        max_frec = 0
        cnt_max_frec = 0
        for n in nums:
            frec_dict[n] += 1
            
            if  frec_dict[n] > max_frec:
                max_frec = frec_dict[n]
                cnt_max_frec = frec_dict[n]
                continue
            
            if frec_dict[n] == max_frec:
                cnt_max_frec += frec_dict[n]

        return cnt_max_frec



























#-------------------------------------------------------------------------------

#         hashMap = defaultdict(int)

#         for n in nums:
#             hashMap[n] += 1
            
#         maxFrecuency = max(hashMap.values())
#         count_maxFrecuency = 0
        
#         for frec in hashMap.values():
#             if frec == maxFrecuency:
#                 count_maxFrecuency += 1
        
#         return count_maxFrecuency*maxFrecuency


#----------------------------------------------------------------------
        # freq=[0]*101
        # maxF=0
        # for x in nums:
        #     freq[x]+=1
        #     maxF=max(maxF, freq[x])
        # ans=0
        # for f in freq:
        #     if f==maxF:
        #         ans+=f
        # return ans
                