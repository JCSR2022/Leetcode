class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        brokenLettersSet = set( [ch for ch in brokenLetters ])

        count = 0
        for word in text.strip().split():
            if any( ch in brokenLettersSet for ch in word ):
                continue
            count +=1

        return count

        
