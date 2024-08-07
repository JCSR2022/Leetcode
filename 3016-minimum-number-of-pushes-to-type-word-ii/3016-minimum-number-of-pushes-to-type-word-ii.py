class Solution:
    def minimumPushes(self, word: str) -> int:
        #aproach:
        # make a cont of letter
        # sort the cont
        # mod the cosrt arr , mult by mode the repited letters count//

        
        cont_lett = Counter(word)
        vect = [(k,v) for k,v in cont_lett.items()]
        vect.sort(key = lambda x:x[1] , reverse =True)

        digits = 8
        ans = 0
        #keypad = [[] for _ in range(digits)]

        for i,(letter,cont) in enumerate(vect):
            #keypad[i%digits].append(letter)
            ans +=  cont*(i//digits +1)  

        #print(ans)
        #print(keypad)
        return ans
        
        
#         cont_lett = Counter(word)
#         ans = 0
#         for i,cont_letter  in enumerate(sorted(cont_lett.values(),reverse = True)):
#             ans +=  cont_letter*(i//8 +1)  
#         return ans
        
        
        
        
        
#         letters = list('abcdefghijklmnopqrstuvwxyz')
#         cont_lett = [0]*len(letters)
        
#         for l in word:
#             cont_lett[letters.index(l)] +=1
#         #print(letters)
#         #print(cont_lett)
        
#         cont_lett.sort(reverse = True)
#         #print(cont_lett)
        
#         ans = 0
#         for i,cont in enumerate(cont_lett):
#             ans +=  cont*(i//8 +1)
#             #print(i,cont,i//8 +1 ,ans)
#         return ans
        