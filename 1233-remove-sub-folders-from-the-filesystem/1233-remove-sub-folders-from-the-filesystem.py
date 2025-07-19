# class trie_folders:
#     def __init__(self):
#         curr_folder_level = {}
#         sub_folder = {}

#     def exist_folder(self,folder):
#         if folder in self.curr_folder_level:
#             if self.curr_folder_level[folder]:
#                 return True
#         return False

    
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False  # marks if a folder ends here


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:


        root = TrieNode()
        folder.sort()  # important to insert parent folders before children
        res = []

        for path in folder:
            parts = path.split("/")[1:]  # skip the empty string before first /
            node = root
            skip = False

            for part in parts:
                if node.end:
                    skip = True  # already covered by a parent
                    break
                if part not in node.children:
                    node.children[part] = TrieNode()
                node = node.children[part]

            if not skip:
                node.end = True
                res.append(path)

        return res

#------------------------------------------------------------------
        # #brute_force:

        # folder.sort()
        # ans = []
        # prev_ans = set()
        # for f in folder:
        #     split_f = "".join(f.split("/"))
        #     not_in_ans = True
        #     for add_f in prev_ans:
        #         if add_f in split_f:
        #             not_in_ans = False
        #     if not_in_ans:
        #         prev_ans.add(f)
        #         ans.append(f)    

        # # return ans

#una mierda maldito imbecil!!!!!!
#---------------------------------------------------------------
#------------------------------------------------------------------------
        # folder_set = set(folder)
        # res = []
        # #print(folder_set)
        # for f in folder:
        #     res.append(f)
        #     #print(res)
        #     for i in range(len(f)):
        #         if f[i] == "/" and f[:i] in folder_set:
        #             res.pop()
        #             break
        
        # return res
#----------------------------------------------------------------
    #build a trie ????






