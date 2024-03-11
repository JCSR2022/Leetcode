class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        # brute force aproach:
        # move thru order, find match in s put in ans
        
        #better: hash table
        # move thru s safe in hashtable appearances, then move thru order with the amount
        # itertools count 
        ans = ""
        hashtable = Counter(s)
        
        
        for letter in order:
            if letter in hashtable:
                ans += letter*hashtable[letter]
                del hashtable[letter]
        
        for letter,rep in hashtable.items():
            ans += letter*rep
            
        return ans
        
            
            
        