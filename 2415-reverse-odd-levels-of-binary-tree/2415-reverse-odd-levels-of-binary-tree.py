# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #direct aproach BFC
              
        q = deque([root])
        level = 1
        
        while q:
            if level % 2 == 0:
                l = 0
                r = len(q)-1
                while l < r:
                    q[l].val,q[r].val = q[r].val,q[l].val
                    l += 1
                    r -= 1
                
            
            elem_in_q = len(q)
            for _ in range(elem_in_q):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level += 1      
            # temp = []
            # for node in q:
            #     temp.append(node.val)
            # print(level,temp)
                
        
        return root
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#-------------------------------------------------------------        
        
        #brute force: 
        # dfs with levels, build new tree
        
#         tree = {}
        
#         def dfs(node,level):
#             if node:
#                 if level in tree:
#                     tree[level].append(node.val)
#                 else:
#                     tree[level] = [node.val]
                    
#             if node.left: dfs(node.left,level+1)
#             if node.right: dfs(node.right,level+1)
        
            
#         def reconstruct_tree(tree):
#             if not tree:
#                 return None

#             # Crear la raíz del árbol
#             root = TreeNode(tree[0][0])
#             queue = [(root, 0)]  # Cola para procesar nodos (nodo, nivel)

#             while queue:
#                 node, level = queue.pop(0)

#                 # Procesar el hijo izquierdo
#                 if level + 1 in tree and tree[level + 1]:
#                     left_val = tree[level + 1].pop(0)
#                     node.left = TreeNode(left_val)
#                     queue.append((node.left, level + 1))

#                 # Procesar el hijo derecho
#                 if level + 1 in tree and tree[level + 1]:
#                     right_val = tree[level + 1].pop(0)
#                     node.right = TreeNode(right_val)
#                     queue.append((node.right, level + 1))

#             return root

                
        
        
#         dfs(root,0)
#         print(tree)
        
#         for k,v in tree.items():
#             if k%2 != 0:
#                 tree[k] = v[::-1]
                
#         new_root = reconstruct_tree(tree)
        
        
#         return new_root
    
    
