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


        #reduce sol
#         hash_s1= Counter(s1.split())
#         hash_s2= Counter(s2.split())
    
#         return [  k1 for  k1,v1 in hash_s1.items() if v1 == 1 and k1 not in hash_s2 ] + [  k2 for  k2,v2 in hash_s2.items() if v2 == 1 and k2 not in hash_s1 ] 


        return self.uncommonFromSentences(s1, s2)

    
    def appendUnCommon(self, l, mul, uc) :
        for s in l :
            if l.count(s) > 1 :
                continue
            if s in mul :
                continue
            uc.append(s)
            
            
    def uncommonFromSentences(self, s1, s2):
        ls1, ls2 = s1.split(" "), s2.split(" ")
        mul = list(set(ls1) & set(ls2))
        uc = []
        
        self.appendUnCommon(ls1, mul, uc)
        self.appendUnCommon(ls2, mul, uc)
        
        return uc 
    
    