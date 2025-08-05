class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        #brute force n**2
 
        n =len(fruits)
        available = [True]*n
        ans = 0

        for cnt_fru in fruits:
            basketFound = False    
            for i in range(n):
                if baskets[i] >= cnt_fru and available[i]:
                    basketFound = True
                    available[i] = False
                    break
            if not basketFound:
                ans +=1

        return ans

