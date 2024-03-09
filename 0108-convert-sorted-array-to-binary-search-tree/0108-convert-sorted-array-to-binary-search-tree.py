# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # begin at the middle of the array
        #buld the left branch inserting values 
        # and then buld the rigth branch
        
        
        def divideTravelGenerator(arr):
            if len(arr) > 1:
                yield arr[len(arr)//2]
                yield from divideTravelGenerator(arr[:len(arr)//2])
                yield from divideTravelGenerator(arr[len(arr)//2+1:])
            elif len(arr) == 1:
                yield arr[0]



        def inputValInBST(node,val):
            if val < node.val:
                if node.left:
                    inputValInBST(node.left,val)
                else:
                    newNode = TreeNode()
                    newNode.val = val
                    node.left = newNode
            else:
                if node.right:
                    inputValInBST(node.right,val)
                else:
                    newNode = TreeNode()
                    newNode.val = val
                    node.right = newNode


        divTravel = divideTravelGenerator(nums)
        for i,val in enumerate(divTravel):
            if i == 0:
                root =  TreeNode()
                root.val = val 
            else:
                inputValInBST(root,val)
        
        return root
        
        
        
        