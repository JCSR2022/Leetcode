# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
#         # aproach: dfs check valid BST on every node
        
        
#         ans = True
        
#         def dfs_check_BST(node):
            
#             nonlocal ans
            
#             if node:
#                 if node.left  and node.left.val  >= node.val: ans = False
#                 if node.right and node.right.val <= node.val: ans = False

#                 dfs_check_BST(node.left)
#                 dfs_check_BST(node.right)

            
#         dfs_check_BST(root)
        
#         return ans
# NO FUNCIONA






#         # 2do aproach 0(n) in fact 3*n:
#         # dfs and bulild the list of values to insert on a new BST
#         # move thru new and old BST if diference return False
        
        
        
        
#         def insert_in_tree(val,level,tree):
#             if level in tree:
#                 tree[level].append(val)
#             else:
#                 tree[level] = [val]
            
            
#         def dfs_saveTree(node,tree,level=0):
#             if node: 
#                 insert_in_tree(node.val,level,tree)
#                 dfs_saveTree(node.left,tree,level+1)
#                 dfs_saveTree(node.right,tree,level+1)
#             else:
#                 insert_in_tree(None,level,tree)
         
        
        
#         org_tree = {}
#         dfs_saveTree(root,org_tree) 
#         # print(org_tree)
         
        
        
#         def insert_in_BST(val,node):
#             if val < node.val:
#                 if not node.left:
#                     l_node = TreeNode(val)
#                     node.left = l_node
#                 else:
#                     insert_in_BST(val,node.left)
#             elif val > node.val:
#                 if not node.right:
#                     r_node = TreeNode(val)
#                     node.right = r_node
#                 else:
#                     insert_in_BST(val,node.right)

                    
        
#         tree_to_create = []
#         for level_val in org_tree.values():
#             tree_to_create +=  level_val
        
#         # print(tree_to_create)
        
#         new_root =  TreeNode(tree_to_create[0])
        
#         for val in tree_to_create[1:]:
#             if val is not None:
#                 insert_in_BST(val,new_root)
        
        
        
#         new_tree = {}
#         dfs_saveTree(new_root,new_tree)     
#         # print(new_tree)
    
        
#         return new_tree == org_tree


# 3rd aproach DFS but with boundries l and r


        ans = True
        
        def dfs_boundries(node,l=-inf,r=inf):
            
            nonlocal ans
            
            if node:
                # print(l,node.val,r)
                if l < node.val < r:
                
                    dfs_boundries(node.left,l,node.val)
                    dfs_boundries(node.right,node.val,r)
  
                else:
                    ans = False
        
        dfs_boundries(root)
        
        return ans     
                
                
                
        
        
        