class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        # # brute force:
        # cont = 0 
        # for i in range(len(arr)-1):
        #     for j in range(i+1,len(arr)):
        #         a = reduce(lambda x, y: x ^ y, arr[i:j])
        #         for k in range(j,len(arr)):
        #             b = reduce(lambda x, y: x ^ y, arr[j:k+1])
        #             print(i,j,k,arr[i:j],arr[j:k+1],a,b,a==b)
        #             if a == b:
        #                 cont += 1        
        # return cont

        
        # # O(n**3) sol
        # cont = 0 
        # for i in range(len(arr)-1):
        #     a = 0
        #     for j in range(i+1,len(arr)):
        #         a ^= arr[j-1]
        #         b = 0
        #         for k in range(j,len(arr)):
        #             b ^= arr[k]
        #             #print(i,j,k,arr[i:j],arr[j:k+1],a,b,a==b)
        #             if a == b:
        #                 cont += 1        
        # return cont        

        
        # usign xor propeties (two pointers) n**2
        
        cont = 0
        for x in range(len(arr)-1):
            temp_xor = arr[x]
            for y in range(x+1,len(arr)):
                temp_xor ^= arr[y]
                if temp_xor == 0:
                    cont += y-x
                    
        return cont
                    
                    
                
        
        
        
        
        
                    
        
        