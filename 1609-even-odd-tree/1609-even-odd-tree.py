# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        if root.val%2 == 0:
            return False
        
        
        #DFS
        # safe on dicc the positions and values of the nodes check condition according
        
        level = [0]
        levelsValues = {}
        #testToPrint = {}
        
        def CheckValLevel(val,level):
            
            if level in levelsValues:
                
                #testToPrint[level].append(val)
            
                if level%2 == 0:
                    #odd-indexed level  even values
                    if val%2 == 0: 
                        return False
                    else: 
                        # even integer values in strictly decreasing order (from left to right).
                        if val <= levelsValues[level][-1]: 
                            return False
                        else:
                            levelsValues[level][-1] = val
                            return True
                
                else:
                    # even-indexed level all nodes odd
                    if val%2 == 0:
                        # odd integer values in strictly increasing order (from left to right).
                        if val >= levelsValues[level][-1]: 
                            return False
                        else:
                            levelsValues[level][-1] = val
                            return True
                    else: 
                        return False
            else:
                if (level%2 == 0 and val%2 != 0) or (level%2 != 0 and val%2 == 0):
                    levelsValues[level] = [val]
                    #testToPrint[level]  = [val]
                    return True
                else:
                    return False
                
        
        
        checkifValLevel = [True]
        def dfs(node):
            if checkifValLevel[0]: checkifValLevel[0] = CheckValLevel(node.val,level[0])
           # print(node.val,level[0],checkifValLevel[0],levelsValues,testToPrint)
            if checkifValLevel[0]:
            
                level[0] +=1

                if node.left: dfs(node.left)
                if node.right: dfs(node.right)

                level[0] -=1
                
        dfs(root)
        
        return    checkifValLevel[0]
            
            
            
        
        
       