class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        drinked = 0
        while numBottles >= numExchange:
            
            temp = numBottles // numExchange
            
            drinked += temp * numExchange
            numBottles = temp + numBottles % numExchange
            
        drinked += numBottles % numExchange
        
        return drinked
        