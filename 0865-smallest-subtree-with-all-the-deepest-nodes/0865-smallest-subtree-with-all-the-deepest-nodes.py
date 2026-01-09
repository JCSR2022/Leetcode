# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def dfs(node):
            if not node: 
                return 0,None
            
            deep_l,node_l = dfs(node.left)
            deep_r,node_r = dfs(node.right)

            if deep_l == deep_r:
                return deep_l+1,node

            elif deep_l > deep_r:
                return  deep_l+1,node_l
            
            else:
                return deep_r+1,node_r


        deep,deep_node = dfs(root)

        return deep_node








        # def dfs(node):

        #     if node.left and node.right:
        #         deep_l,node_l = dfs(node.left)
        #         deep_r,node_r = dfs(node.right)

        #         if deep_l == deep_r:
        #             return deep_l+1,node
        #         elif deep_l > deep_r:
        #             return deep_l,node_l
        #         else:
        #             return deep_r,node_r

        #     elif node.left:
        #         return dfs(node.left)

        #     elif node.right:
        #         return dfs(node.right)
            
        #     return 1,node
            
            
        # _ , deep_node = dfs(root)


        # return deep_node
                

            

              







            



                



            







#----------------------------------------------------------
        #make dfs but return the deep of the branch, 
        # def dfs(node,deep):
        #     print(node.val,
        #             node.left.val if node.left else None,
        #             node.right.val if node.right else None ,
        #             deep)

        #     left_deep = deep
        #     right_deep = deep

        #     if node.left:
        #         left_deep,left_deep_node = dfs(node.left,deep+1) 
        #     if node.right:
        #         right_deep,right_deep_node = dfs(node.right,deep+1) 
            
        #     if node.left and left_deep < right_deep:
        #         return left_deep,left_deep_node
            
        #     if node.right and left_deep > right_deep:
        #         return right_deep,right_deep_node

            
        #     return left_deep,node
            
        # deep,root_deep = dfs(root,0)
        # return root_deep

#eres un maldito retrasado mental de mierda, espero te mueras pronto para que se acabe tu sufrimiento, imbecil!!!!!!!
#---------------------------------------------------------------------