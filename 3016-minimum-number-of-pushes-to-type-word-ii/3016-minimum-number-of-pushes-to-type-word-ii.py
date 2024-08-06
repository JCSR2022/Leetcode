class Solution:
    def minimumPushes(self, word: str) -> int:
        #aproach:
        # make a cont of letter
        # sort the cont
        # mod the cosrt arr , mult by mode the repited letters count//
        
        #cont_lett = Counter(word)
        
        letters = list('abcdefghijklmnopqrstuvwxyz')
        cont_lett = [0]*len(letters)
        
        for l in word:
            cont_lett[letters.index(l)] +=1
        #print(letters)
        #print(cont_lett)
        
        cont_lett.sort(reverse = True)
        #print(cont_lett)
        
        ans = 0
        for i,cont in enumerate(cont_lett):
            ans +=  cont*(i//8 +1)
            #print(i,cont,i//8 +1 ,ans)
        return ans
        