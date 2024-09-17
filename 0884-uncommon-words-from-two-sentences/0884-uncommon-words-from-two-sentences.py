class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # hash sentence, compare 1 ocurence words
        
#         hash_s1 = defaultdict(int)
#         for s in s1.split():
#             hash_s1[s] +=1
        
#         hash_s2 = defaultdict(int)
#         for s in s2.split():
#             hash_s2[s] +=1
                
#         ans1 = [  k1 for  k1,v1 in hash_s1.items() if v1 == 1 and k1 not in  hash_s2 ]
#         ans2 = [  k2 for  k2,v2 in hash_s2.items() if v2 == 1 and k2 not in  hash_s1 ]
        
#         return ans1+ans2


        hash_s1= Counter(s1.split())
        hash_s2= Counter(s2.split())
    
        return [  k1 for  k1,v1 in hash_s1.items() if v1 == 1 and k1 not in  hash_s2 ] + [  k2 for  k2,v2 in hash_s2.items() if v2 == 1 and k2 not in  hash_s1 ] 