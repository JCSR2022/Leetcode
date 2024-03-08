# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        #The worst way to do it, not brute force but mega brute force
        # save all values in a list
        # sort the list
        # find min distance between values
        
        
        # null case:
        if not root:
            return root
        
       
        values = []
        
        def dfs(node):
            values.append(node.val)
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
        
        dfs(root)
        values.sort()
        
         # minimum absolute difference
        minBetweenVal = float(inf)
        for i in range(1,len(values)):
            minBetweenVal = min(minBetweenVal, values[i]-values[i-1] )
        
        
        
        return minBetweenVal
            
        
        