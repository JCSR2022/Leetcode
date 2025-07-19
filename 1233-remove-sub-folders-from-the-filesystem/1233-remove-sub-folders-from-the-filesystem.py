class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

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
        folder_set = set(folder)
        res = []
        #print(folder_set)
        for f in folder:
            res.append(f)
            #print(res)
            for i in range(len(f)):
                if f[i] == "/" and f[:i] in folder_set:
                    res.pop()
                    break
        
        return res