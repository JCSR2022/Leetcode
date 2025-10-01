class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        #dp?
        
        drinked = numBottles
        empthy = numBottles
        while  empthy//numExchange > 0:
            numBottles = empthy//numExchange
            drinked += numBottles
            empthy = numBottles + empthy%numExchange

        return drinked





















































        # drinked = 0
        # while numBottles >= numExchange:
        #     # print(numBottles,numBottles // numExchange,drinked)
        #     temp = numBottles // numExchange
        #     drinked += temp * numExchange
        #     numBottles = temp + numBottles % numExchange
            
        # drinked += numBottles % numExchange
        
        # return drinked
        