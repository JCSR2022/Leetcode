# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        #bruteforce dfs, save levels sum, sort, find the kth
        
        levels_sum = defaultdict(int)
        
        def dfs(node,level):
            if node:
                levels_sum[level] += node.val  
                dfs(node.left,level+1)
                dfs(node.right,level +1)
        
        dfs(root,1)
        
        #if want to return the level
        
        ans = [(k,v) for k,v in levels_sum.items() ]  
        ans.sort(key=lambda x:x[1],reverse =True)
        if len(ans) < k:
            return -1
        else:
            return ans[k-1][1]
        
        
        
#         ans = sorted(levels_sum.values(), reverse=True)
#         if len(ans) < k:
#             return -1
#         else:
#             return ans[k-1] 
        
            
       

            
            
            