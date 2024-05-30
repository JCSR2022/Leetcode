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

        
        
        
        
        
#         # usign xor propeties n**2
        
#         cont = 0
#         for x in range(len(arr)-1):
#             temp_xor = arr[x]
#             for y in range(x+1,len(arr)):
#                 temp_xor ^= arr[y]
#                 if temp_xor == 0:
#                     cont += y-x
                    
#         return cont


# ni en pedo entiendo esta solucion!!!!! O(n) !!!!
    
        N = len(arr)
        res = 0
        prefix = 0
        prev_xor_count = defaultdict(int)
        prev_xor_count[0] = 1
        prev_xor_index_sum = defaultdict(int)
        
        for i in range(N):
            prefix ^= arr[i]
            
            if prev_xor_count[prefix]:
                res += i * prev_xor_count[prefix] - prev_xor_index_sum[prefix] 
            
            
            prev_xor_count[prefix] += 1
            prev_xor_index_sum[prefix] += i + 1
        
        
        return res
        
        
                    
                    
                
        
        
        
        
        
                    
        
        