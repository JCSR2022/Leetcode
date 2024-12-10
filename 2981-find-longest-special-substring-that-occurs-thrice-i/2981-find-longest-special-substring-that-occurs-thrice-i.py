class Solution:
    def maximumLength(self, s: str) -> int:
        
        
        #hashtable
        
        hash_letter = {letter:defaultdict(int) for letter in "abcdefghijklmnopqrstuvwxyz"}
        
        i = 0
        j = 0
        cont_coinc = 0
        
        while j < len(s):   
            if s[i] == s[j]:
                cont_coinc += 1
                for k in range(1,cont_coinc+1):
                    hash_letter[s[i]][k] +=1
                j += 1
            else:
                cont_coinc = 0
                i = j
        
        ans = -1
        for k,v in hash_letter.items(): 
            ans = max(ans,max([ k  for k,v in  hash_letter[k].items() if v >= 3 ]+[-1]))  
        
        return ans
                