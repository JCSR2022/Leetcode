class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        #brute aproach, as you, brute,  hashmap
        
        def find_hash(word):
            hash = {}
            for l in word:
                if l not in hash:
                    hash[l] = 1
                else: 
                    hash[l] += 1
            return hash 
        
        hashWord = find_hash(words[0])
        
        for i in range(1,len(words)):
            Newhash = find_hash(words[i])

            for key,val in hashWord.items():
                if key in Newhash:
                    hashWord[key] = min(hashWord[key],Newhash[key])
                else:
                    hashWord[key] = 0
                    
                
        ans = []        
        
        for key,val in hashWord.items():
            if val > 0:
                ans += [key]*val
        
        return ans
            
            
            