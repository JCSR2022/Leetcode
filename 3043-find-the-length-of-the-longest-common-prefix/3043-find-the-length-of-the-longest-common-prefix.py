class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        #brute force:
        
        
#         def find_prefix_val(num1,num2):
#             str_num1 = str(num1)
#             str_num2 = str(num2)
            
#             cont = 0 
#             for dig1,dig2 in zip(str_num1,str_num2):
#                 if dig1 == dig2: 
#                     cont +=1
#                 else: 
#                     break
#             return cont
                    
            
#         max_prefix = 0
#         for num1 in arr1:
#             for num2 in arr2:
#                 max_prefix = max(max_prefix,find_prefix_val(num1,num2))
#         return max_prefix
                                
    
    
#----------------------------------------------------------


        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        prefix_set = set()
        
        for n in arr1:
            while n and n not in prefix_set:
                prefix_set.add(n)
                n = n// 10

        res = 0
        for n in arr2:
            while n and n not in prefix_set:
                n=n// 10
            if n:
                res = max(res, len(str(n)))
        return res

    
    
    
    
    
    
    
    
    
    
#-------------------------------------------------------------                                 
                                 
        #Best otption is to use a Trie and dfs
        
        #Trie data structure - Inside code
        #https://www.youtube.com/watch?v=qA8l8TAMyig
        
        
        
        