from collections import Counter

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        #aproach1:
        # hashmap
        # for each k:val, fill with k-1:val
        
    
       #NOOOOOO, READ @#%@%@%@, HAVE TO BE IN ORDER!!!!!! 
#         hash_bills = Counter(bills)
        
#         cond1 = hash_bills[5] >= hash_bills[10]
#         cond2 = hash_bills[5]-hash_bills[10] >= hash_bills[20]
#         cond3 = hash_bills[10] >= hash_bills[20]  
#         print(hash_bills,cond1,cond2,cond3)
#         return cond1 and cond2 and cond3
        
        #aproach 2:
        # pointer with counts
        
        cont_5  = 0
        cont_10 = 0
        for i,cx in enumerate(bills):
            
            if cx == 5:
                cont_5 +=1
            elif cx == 10:
                cont_5  -= 1
                cont_10 += 1
            elif cx == 20:
                if cont_10 > 0:
                    cont_10 -= 1
                    cont_5  -= 1
                else:
                    cont_5  -= 3
            #print(i,cx,cont_5,cont_10,cont_5 <0 ,cont_10 <0 ,cont_5 < 0 or cont_10 < 0)
            if cont_5 < 0 or cont_10 < 0:
                return False
            
        return True
        
        
        
        
