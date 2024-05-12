class TreeNode:
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        
#         # brute force DFS!! 
        
#         def constructTree(triangle: List[List[int]]) -> TreeNode:
#             # Creamos los nodos del triángulo
#             list_nodes = [[TreeNode(val) for val in row] for row in triangle]

#             # Conectamos los nodos del triángulo en forma de árbol
#             for i in range(len(triangle) - 1):
#                 for j in range(len(triangle[i])):
#                     list_nodes[i][j].left = list_nodes[i + 1][j]
#                     list_nodes[i][j].right = list_nodes[i + 1][j + 1]
            
#             return list_nodes[0][0] 
        
        
#         min_sum_path = float("inf")
#         def dfs_min_path(node,sum_path=0):
#             nonlocal  min_sum_path
            
#             sum_path += node.val
            
#             if node.left is None and node.right == None:
#                 min_sum_path = min(min_sum_path,sum_path)   
#             else:
#                 dfs_min_path(node.left,sum_path)
#                 dfs_min_path(node.right,sum_path)
        
        
#         root = constructTree(triangle)
#         dfs_min_path(root)
        
        
#         return  min_sum_path
        
    
        # dynamic Programing Sol Mem = O(n) , T = O(n**2)
        
        dp = [0] * (len(triangle)+1)
        
        for row in triangle[::-1]:
            for i,n in enumerate(row):
                #print(dp)
                dp[i] = n + min(dp[i],dp[i+1])
        
        return dp[0]
            
                
        
        
        
        