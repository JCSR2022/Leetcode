class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        # sliding window
        
    
        cont_odds = 0
        
        for num in arr:
            if num%2 !=0:
                cont_odds +=1
                if cont_odds == 3:
                    return True
            else:
                cont_odds = 0
        
        return False