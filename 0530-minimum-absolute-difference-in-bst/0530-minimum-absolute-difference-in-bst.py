# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
#         #The worst way to do it, not brute force but mega brute force
#         # save all values in a list
#         # sort the list
#         # find min distance between values
        
        
#         # null case:
#         if not root:
#             return root
        
       
#         values = []
        
#         def dfs(node):
#             values.append(node.val)
#             if node.left: dfs(node.left)
#             if node.right: dfs(node.right)
        
#         dfs(root)
#         values.sort()
        
#          # minimum absolute difference
#         minBetweenVal = float(inf)
#         for i in range(1,len(values)):
#             minBetweenVal = min(minBetweenVal, values[i]-values[i-1] )
            
#         return minBetweenVal
    
        # CORRECT WAY OF DO IT:
        """
        In-order traversal is a depth-first traversal algorithm used to explore the nodes 
        of a  binary tree, particularly Binary Search Trees (BST). 
        The in-order traversal visits the nodes in a specific order:
        Visit the left subtree.
        Visit the current (root) node.
        Visit the right subtree.
        For a BST, this results in visiting the nodes in ascending order of their values
        """
        #values = []
    
        prev = None
        minBetweenVal = float("inf")
        
        def in_order_traversal(node):
            if not node:
                return
            
            nonlocal prev, minBetweenVal
                
            # Visit the left subtree
            if node.left: in_order_traversal(node.left)

            # Visit the current node
            #values.append(node.val)
            if prev:
                minBetweenVal = min(minBetweenVal ,abs(node.val-prev.val))
            prev = node

            # Visit the right subtree
            if node.right: in_order_traversal(node.right)
        
        in_order_traversal(root)
        print(minBetweenVal )
        
        return  minBetweenVal
    
    
    
    
            
        
        