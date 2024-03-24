# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
#         # aproach: dfs saving a count for the nodes on the highest level (maxLevel)
#         # then calculate sum([2**n for n in range(maxLevel-1)]) + nodes on maxLevel 

#         maxLevel = [0]
#         nodesOnMaxLevel = [0]
        
#         def dfs(node,level = 1):
#             if node:
#                 if level > maxLevel[0]:
#                     maxLevel[0] = level
#                     nodesOnMaxLevel[0] = 1
                    
#                 elif level == maxLevel[0]:
#                     nodesOnMaxLevel[0]  += 1
                    
#                 if node.left: dfs(node.left,level + 1)
#                 if node.right: dfs(node.right,level + 1)
                    
#         dfs(root)
#         nodesOnOtherLevels = sum([2**n for n in range(maxLevel[0]-1)])
        
        
#         print( nodesOnMaxLevel[0],nodesOnOtherLevels )
        
        
#         return  nodesOnOtherLevels+ nodesOnMaxLevel[0]



        """stanislav-iablokov"""

        def countNodes(root, l=1, r=1):

            if not root : return 0

            left = right = root                           # compute both left and right heights of
            while left  := left.left   : l += 1           # each subtree by going all way down to
            while right := right.right : r += 1           # the left and right (in logN time)

            if l == r : return 2**l - 1                   # if it's a full tree, its size is known
        
            return 1 + countNodes(root.left) + countNodes(root.right)
        
        return countNodes(root)
        
        


# Python #1. BFS with the traversal of every node. Time/space complexity is linear: O(N).

# dq, m = deque([root]), 0
#         while dq:
#             node = dq.popleft()
#             if node:
#                 m +=1
#                 dq.append(node.left)
#                 dq.append(node.right)
#         return m

# # counting 1 for every node that is not None
#         return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0


                
                    
                    
                
                
     
            
            
        
        