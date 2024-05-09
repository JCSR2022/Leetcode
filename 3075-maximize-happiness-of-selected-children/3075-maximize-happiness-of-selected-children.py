class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness.sort(reverse = True)
        
        h = 0
        i = 0
        while k > 0 and i < len(happiness) and happiness[i]-i > 0:
            h += happiness[i] - i
            i += 1
            k -= 1
        return h
            
        