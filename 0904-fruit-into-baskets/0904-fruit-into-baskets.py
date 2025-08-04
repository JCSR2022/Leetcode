class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        par = {-2,-1}
        curr_max = 0
        glob_max = 0
        prev = {-1:0}

        for f in fruits:
            if f in par:
                curr_max += 1
                if f == list(prev.keys())[0]:
                    prev[f] +=1 
                else:
                    prev = {f:1}
            else:
                par = {list(prev.keys())[0],f}
                curr_max = list(prev.values())[0]+1
                prev = {f:1}
            glob_max = max(glob_max,curr_max)

        return glob_max


        