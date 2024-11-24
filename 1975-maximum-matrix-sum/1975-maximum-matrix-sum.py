class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        #craizy idea:
        # if neg are ood find sum , convert or neg in postive
        # else find abs(min) and substract
        
        absSum = 0
        odd = True
        absMin = float("inf")
    
        for row in matrix:
            for val in row:
                absVal = abs(val)
                absSum += absVal
                if val < 0:  odd = not odd
                absMin = min(absMin, absVal)
                #print(val,val < 0,odd,absMin,absSum)
        
        return absSum if odd else absSum-2*absMin