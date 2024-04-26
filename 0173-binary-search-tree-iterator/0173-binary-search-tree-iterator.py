# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.InOrder = deque([])
        self.dfsInorder(root)
        
    def dfsInorder(self,node):
        if node:
            if node.left: self.dfsInorder(node.left)
            self.InOrder.append(node.val)
            if node.right: self.dfsInorder(node.right)            

    
    def next(self) -> int:
        return self.InOrder.popleft()
            
        
    def hasNext(self) -> bool:
        return len(self.InOrder) != 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()