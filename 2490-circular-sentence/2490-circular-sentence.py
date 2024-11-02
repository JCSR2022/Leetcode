class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
#         if sentence[0] != sentence[-1]:
#             return False
        
#         words = sentence.split()
#         last = words[0] 
#         for word in words[1:]:
#             if last[-1] != word[0]:
#                 return False
#             last = word
        
#         return True



        for i in range(len(sentence)):
            if sentence[i] == " ":
                if sentence[i-1] != sentence[i+1]:
                    return False
        return sentence[0] == sentence[-1]
            