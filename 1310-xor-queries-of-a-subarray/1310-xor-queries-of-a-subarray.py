class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
#         result = []
#         for i,j in queries:
#             #print(i,j,arr[i:j+1] )
#             result.append(functools.reduce(lambda x, y: x ^ y, arr[i:j+1]))
        
#         return result



# time complex O(n)*O(q) = O(n*q) Liniar

        prefix_xor = [0]
        for elem in arr:
            prefix_xor.append(prefix_xor[-1]^elem)

        return  [prefix_xor[i]  ^ prefix_xor[j+1]  for i,j in  queries]