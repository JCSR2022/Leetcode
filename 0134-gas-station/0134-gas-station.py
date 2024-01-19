class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1
        
        size = len(gas)
        suma = 0 
        posicion = 0
        
        for i in range(size):
            suma += gas[i] - cost[i]
            #  print(i,gas[i],cost[i], suma,suma < 0,posicion)
            if suma < 0:
                suma = 0
                posicion = i+1
        
        return posicion

# gas = [5,1,2,4,3,4,1,5,2]
# cost = [1,3,4,2,5,1,5,2,4]
# diff = [ gas_i-cost_i for gas_i,cost_i in zip(gas,cost) ]
        
        