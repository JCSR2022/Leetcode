class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        # brokenLettersSet = set( [ch for ch in brokenLetters ])

        # count = 0
        # for word in text.strip().split():
        #     if any( ch in brokenLettersSet for ch in word ):
        #         continue
        #     count +=1

        # return count

#---------------------------------------------------------------
#improve?????

        counter = 0
        for word in text.split():
            for letter in word:
                if letter in brokenLetters:
                    counter+=1
                    break
        return len(text.split())-counter
        
        
