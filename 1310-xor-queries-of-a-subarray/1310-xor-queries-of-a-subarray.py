class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
#         result = []
#         for i,j in queries:
#             #print(i,j,arr[i:j+1] )
#             result.append(functools.reduce(lambda x, y: x ^ y, arr[i:j+1]))
        
#         return result




        prefix_xor = [0]
        pre_xor = 0
        for i,elem in enumerate(arr):
            pre_xor ^= elem
            #print(arr[0:i+1],functools.reduce(lambda x, y: x ^ y, arr[0:i+1]) , pre_xor )
            prefix_xor.append(pre_xor)
        #print(prefix_xor)
        
        ans = []
        for i,j in  queries:
            #print((i,j+1),prefix_xor[i],prefix_xor[j+1],prefix_xor[i]^prefix_xor[j+1] )
    
            ans.append(prefix_xor[i]  ^ prefix_xor[j+1]) 
            
        return ans