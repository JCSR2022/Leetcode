# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            if left == -1: return -1
            
            right = dfs(node.right)
            if right == -1: return -1
            
            if abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)
            
        return dfs(root) != -1       


#----------------------------------------------------

        # balance = [True]
        # def dfs(node,level):
        #     if balance[0]:
                
        #         if node:
        #             l_level = dfs(node.left,level+1)
        #             r_level = dfs(node.right,level+1)
        #             return level + 1

        #         else:
        #             return level


        #         if node.left:
                     
            
        #         if node.right:
        #             r_level = dfs(node.right,level+1)


#----------------------------------------------------

        # def dfs(node):
        #     if node:

        #         if node.left:
        #             l_level,l_balance = dfs(node.left)
        #         else:
        #             l_level = 0
        #             l_balance = True


        #         if node.right:
        #             r_level,r_balance = dfs(node.right)
        #         else:
        #             r_level = 0
        #             r_balance =True
                
        #         balance = abs(l_level-r_level) < 1 


        #         return max(l_level,r_level), balance & l_balance & r_balance
            
        #     else:
        #         return 0,True


        # max_level,balance = dfs(root)

        # return balance

 

































        # balance = [True]
        # def dfs(node):

        #     if balance[0]:

        #         l_deep = 1
        #         if node.left:
        #             l_deep += dfs(node.left)
                    
        #         r_deep = 1
        #         if node.right:
        #             r_deep =+ dfs(node.right)

        #         if abs(l_deep-r_deep) > 1:
        #             balance[0] = False


        # return balance[0]
            