class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        #dinamic programin aproach, botom up aproach
        def WordsInDict(i,s,wordDict):
            posibles = []
            for word in wordDict:
                if s[i] == word[0]:
                    if s[i:i+len(word)] == word:
                        posibles.append(word)
            return posibles
        
        dp = [False]*len(s)
        dp.append(True)
        
        for i in range(len(s)-1,-1,-1):
            words = WordsInDict(i,s,wordDict)
            #print(i,s[i],words,dp)
            if words:
                for word in words:
                    dp[i] = dp[i] | dp[i+len(word)] 
        
        #print(dp)
        
        return dp[0]
        