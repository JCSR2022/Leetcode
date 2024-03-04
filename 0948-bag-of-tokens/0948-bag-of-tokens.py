class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        # two pointers: Time O[nLog(n)] n = len(tokens) 
        #  L = 0, R = len(tokens)-1 
        #  order tokens
        #  while L<=R:
        #  if tokens[L]<power  faceUp: score +=1, L +=1 , power -= tokens[L] 
        #  else:
        #     if score > 0      faceDown:  score -=1  R -=1 ,  power += tokens[R] 
        #       else End 
        
        #Trivial sol:
        if len(tokens) == 0:
            return 0
        if len(tokens) == 1:
            if tokens[0] < power:
                return 1
            else:
                return 0
        
        score = 0
        L = 0 
        R = len(tokens)-1
        tokens.sort()
        
#         while L<=R:
#             print(L,R,tokens[L],tokens[R],power,score)
#             if tokens[L] <= power:
#                 #faceUp: 
#                 score +=1
#                 power -= tokens[L]
#                 L +=1  
#             else:
#                 if score > 0 and L < R:
#                     #faceDown:  
#                     score -=1  
#                     power += tokens[R] 
#                     R -=1
#                 else:
#                     return score
                
#        return score
         
    
        ans = 0
        while L<=R:
            #print(L,R,tokens[L],tokens[R],power,score)
            if tokens[L] <= power:
                #faceUp: 
                score +=1
                power -= tokens[L]
                L +=1  
                ans = max(ans,score)
            elif score > 0:
                    #faceDown:  
                    score -=1  
                    power += tokens[R] 
                    R -=1
            else:
                return ans

        return ans 
                    
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        