class Trie:

    def __init__(self):
        self.children = defaultdict(Trie)
        self.delete = False
    
    def add(self, list_element):
        curr = self
        for element in list_element:
            curr = curr.children[element]

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        
        # root = Trie()
        # for path in paths:
        #     root.add(path)

        # seen = defaultdict(list)
        # def  dfs_serialize(trie):
        #     if not trie.children:
        #         return "" 
        #     s = []
        #     for folder, child in trie.children.items():
        #         s.append(folder+dfs_serialize(child))
        #     key = "".join(s)
        #     seen[key].append(trie)

        #     # for k,v in seen.items():
        #     #     print(k,v)
        #     # print()

        #     return key



        # dfs_serialize(root)
        # for nodes in seen.values():
        #     if len(nodes) >=2:
        #         for node in nodes:
        #             node.delete = True
        
        # res = []
        # def dfs_delete(node,path):
        #     for folder, child in node.children.items():
        #         if not child.delete:
        #             curr = path + [folder]
        #             res.append(curr)
        #             dfs_delete(child,curr)
        
        # dfs_delete(root,[])
        # return res





#----------------------------------------------------------------------
        root = Trie()
        for path in sorted(paths):
            root.add(path)

        seen = defaultdict(list)
        def  dfs_serialize(trie):
            if not trie.children:
                return "" 
            s = []
            for folder, child in trie.children.items():
                s.append(folder+'('+dfs_serialize(child)+')')
            key = "".join(s)
            seen[key].append(trie)
            return key

        dfs_serialize(root)
        for nodes in seen.values():
            if len(nodes) >=2:
                for node in nodes:
                    node.delete = True
        
        res = []
        def dfs(node,path):
            for folder, child in node.children.items():
                if not child.delete:
                    curr = path + [folder]
                    res.append(curr)
                    dfs(child,curr)
        
        dfs(root,[])
        return res




