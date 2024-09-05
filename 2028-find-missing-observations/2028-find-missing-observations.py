class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        #Aproach, :
        # mean = suma / k  , where k = len(rolls)+n , suma = mean*(len(rolls)+n) 
        # but suma = suma_rolls + suma_n  => suma_n = mean*(len(rolls)+ n ) - suma_rolls
        # if suma_n < n or suma_n > n*6 return []
        # create arr full 1, add each cell unitill get to 6 and untill reach suma_n
        
        
        suma_n = mean*(len(rolls)+n) - sum(rolls)
        
        if suma_n < n or suma_n > n*6:
            return []
        
        
        n_arr = [suma_n//n]*n
        suma_n -= (suma_n//n)*n
        i = 0
        #print(n_arr,suma_n)
        
        while suma_n != 0:
            n_arr[i] += 1
            suma_n -= 1
            if n_arr[i] == 6:
                i += 1    
        
#         n_arr = [1]*n
#         suma_n -= n
#         i = 0
#         while suma_n != 0:
#             n_arr[i] += 1
#             suma_n -= 1
#             if n_arr[i] == 6:
#                 i += 1
                
        return n_arr 