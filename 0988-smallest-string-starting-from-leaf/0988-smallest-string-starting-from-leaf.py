# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # Aproach: DFS, memory of branch, chek min when leaf
        
        if not root:
            return ''
    
    
        def compare(arr1,arr2):
            n = min(len(arr1),len(arr2))
            for i in range(n):
                if arr1[i]<arr2[i]:
                    return arr1
                elif arr1[i]>arr2[i]:
                    return arr2
            
            if len(arr1) < len(arr2):
                return arr1
            else:
                return arr2
            
    
        smallest = None
        
        def dfs(node,branch=[]):
            
            nonlocal smallest
        
            branch.append(node.val)
            
            if not node.left and not node.right:
                # temp = ""
                # for n in branch[::-1]:
                #     temp += chr(97+n)
                # print(temp)
                
                if not smallest:
                    smallest =  branch[::-1]
                else:
                    smallest = compare(branch[::-1],smallest)
            else:
                if node.left: dfs(node.left,branch)
                if node.right: dfs(node.right,branch)
            branch.pop()
            
 
        dfs(root)
        
        ans = ""
        for n in smallest:
            ans += chr(97+n)
        
        return ans