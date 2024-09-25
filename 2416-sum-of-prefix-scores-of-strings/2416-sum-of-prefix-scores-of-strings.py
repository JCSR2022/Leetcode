class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        #brute force
        #build a hash map of all prefix for each word, add +1 on every apeance
        
        
        prefix_aperance = Counter()
        
        for w in words:
            for prefix in [ w[:i+1] for i in range(len(w))]:
                prefix_aperance[prefix] +=1
                
        #print(prefix_aperance )
        
        ans = [0]*len(words)
        for i,w in  enumerate(words):
            for prefix in [ w[:i+1] for i in range(len(w))]:
                ans[i] +=prefix_aperance[prefix] 
                
                
        return ans
            
            