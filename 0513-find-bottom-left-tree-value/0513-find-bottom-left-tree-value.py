# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        
        actual =   [0,0,root.val] # [rowOfTree,columnOfTree,value]
        mostLeft = [0,0,root.val] # [rowOfTree,columnOfTree,value]
        
        
        def most_Left_Leaf(actual,mostLeft):
            if actual[0] >  mostLeft[0]:
                mostLeft[:] = actual[:]
            # elif(actual[0] ==  mostLeft[0]):
            #     if actual[1] < mostLeft[1]:
            #         mostLeft[1:] = actual[1:]
                    
                    
        # DFS
        def dfs(node):
            actual[2] = node.val
            print(actual, mostLeft)
            most_Left_Leaf(actual,mostLeft)

            actual[0] +=1

            actual[1] -=1
            if node.left: dfs(node.left)
            actual[1] +=1

            actual[1] +=1
            if node.right: dfs(node.right)
            actual[1] -=1
            
            actual[0] -=1



            

        dfs(root)
            
        return mostLeft[2]
                    
                    
                    
                    
                    
                    
                    
                    
                
                
                 
        
        