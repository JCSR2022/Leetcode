class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        size = len(gas)
        suma = 0 
        posicion = 0
        
        for i in range(size):
            suma += gas[i] - cost[i]
            if suma < 0:
                suma = 0
                posicion = i+1
        
        return posicion
                
                
        
        