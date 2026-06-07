# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:


        #use some kind of union-join??

        #   root   nodes 
        #   none    {}
        #   20      {20,15}
        #   20      {20,15,17}
        #   50      {20,15,17,50}
        #   50      {20,15,17,50,80 }
        #   50      {20,15,17,50,80,19 }
#-----------------------------------------------        
        #   85      {85,82}
        #   74      {85,82,74}
        #   39      {85,82,74,39,70}
        #   39      {85,82,74,39,70,38}
        #   39      {85,82,74,39,70,38}



        nodes = {}
        childs = set()

        for parenti, childi, isLefti in descriptions:
            if parenti not in nodes:
                nodes[parenti] = TreeNode(parenti)

            childs.add(childi)
            if childi not in nodes:
                nodes[childi] = TreeNode(childi)

            if isLefti:
                nodes[parenti].left = nodes[childi]
            else:
                nodes[parenti].right = nodes[childi]


        root = [ node for node in nodes if node not in childs ]

        return nodes[root[0]]
        