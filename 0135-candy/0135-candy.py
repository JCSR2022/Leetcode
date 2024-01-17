class Solution:
    def candy(self, ratings: List[int]) -> int:
        size = len(ratings)
        
        if size == 1:
            return 1
    
        if size == 2:
            if ratings[0] == ratings[1]:
                return 2
            else:
                return 3
            
       # size > 2
        candies = [1]*size
        for i in range(1,size):
            if ratings[i -1] < ratings[i]:
                candies[i] = candies[i-1] + 1
                
        for i in range(size-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i],candies[i+1]+1)
        return sum(candies)
        