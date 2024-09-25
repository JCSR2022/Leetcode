class TrieNode:
    def __init__(self):
        self.children = {}
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,num):
        node = self.root
        
        for n in str(num):
            if n not in node.children:
                node.children[n] = TrieNode()
            node = node.children[n]

            
    def find_count(self, num):
#         node = self.root
#         for i,n in enumerate(str(num)):
#             if n not in node.children:
#                 break
#             node = node.children[n]
#         return i

        node = self.root
        length = 0  # Tracks length of common prefix
        for n in str(num):
            if n in node.children:
                node = node.children[n]
                length += 1  # Increment the prefix length if a match is found
            else:
                break  # Stop when characters don't match
        return length  # Return the length of the common prefix
            
            

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        trie =  Trie()
        
        for num in arr1:
            trie.insert(num)
        
        max_prefix = 0
        for num in arr2:
            max_prefix = max(max_prefix,trie.find_count(num))
            
        return max_prefix
        
        
        
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


#         if len(arr1) > len(arr2):
#             arr1, arr2 = arr2, arr1

#         prefix_set = set()
        
#         for n in arr1:
#             while n and n not in prefix_set:
#                 prefix_set.add(n)
#                 n = n// 10

#         res = 0
#         for n in arr2:
#             while n and n not in prefix_set:
#                 n=n// 10
#             if n:
#                 res = max(res, len(str(n)))
#         return res

    
    
    
    
    
# ----------------------------------------------------------

        #Best option is to use a Trie and dfs????
        
        #Trie data structure - Inside code
        #https://www.youtube.com/watch?v=qA8l8TAMyig
        
        #Basics of trie
        #https://www.youtube.com/watch?v=6PX6wqDQE20
        
        

        
        
        
        
        
        
        
        
        
        