class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        list_sentence = sentence.split()
        
        ans = -1
        
        for i,word in enumerate(list_sentence):
            if word.startswith(searchWord):
                ans = i+1
                break
                
        return ans
        