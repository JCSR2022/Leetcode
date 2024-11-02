class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        if sentence[0] != sentence[-1]:
            return False
        
        words = sentence.split()
        last = words[0] 
        for word in words[1:]:
            if last[-1] != word[0]:
                return False
            last = word
        
        return True
            