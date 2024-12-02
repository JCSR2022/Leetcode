class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
       
#        list_sentence = sentence.split()
        
#         ans = -1
        
#         for i,word in enumerate(list_sentence):
#             if word.startswith(searchWord):
#                 ans = i+1
#                 break
                
#         return ans

#---------------------------------------------
        cont_w = 1
        cont_match = 0
        new_word = True
        for letter in sentence:
            if letter == " ":
                cont_w += 1
                new_word = True
                cont_match = 0
                continue
            
            if new_word and letter == searchWord[cont_match]:
                cont_match +=1
                if cont_match == len(searchWord):
                    return cont_w
            else:
                new_word = False
        
        return -1
                    
            
        