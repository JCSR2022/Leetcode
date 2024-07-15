# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        #make hashmap relation nodes
        
        hashNodes = {}
        nodes_parent = []
        for node in descriptions:
            #print(node[0],node[1],node[2])
            if node[0] not in hashNodes:
                hashNodes[node[0]] = TreeNode(node[0])
            if node[1] not in hashNodes:
                hashNodes[node[1]] = TreeNode(node[1])
            
            nodes_parent.append(node[1])
            if node[2] == 0:
                hashNodes[node[0]].right= hashNodes[node[1]]
            else:
                hashNodes[node[0]].left= hashNodes[node[1]]
                
        for node in hashNodes.keys():
            if node not in nodes_parent:
                return hashNodes[node] 
        
        