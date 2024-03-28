# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        val = postorder[-1]
        
        #print("val:",val,", index:",inorder.index(val))

        leftInorder = inorder[:inorder.index(val)]
        rightInorder =  inorder[inorder.index(val)+1:]
        leftPostOrder =  postorder[:len(leftInorder)]
        rightPostOrder = postorder[len(leftInorder):-1]

        #print("leftInorder:",leftInorder,", rightInorder:",rightInorder)
        #print("leftPostOrder:",leftPostOrder,", rightPostOrder:",rightPostOrder)
        #print()
        
        root = TreeNode(val)
        
        if len(leftInorder) > 0: 
            root.left = self.buildTree(leftInorder,leftPostOrder)
        else:
            root.left = None
        
        if len(rightInorder) > 0:
            root.right = self.buildTree(rightInorder,rightPostOrder)
        else:
            root.right = None
            
        return root
        
            
        
        
        
        
        