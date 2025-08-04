class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        # O(n)

        par = {-2,-1}
        curr_max = 0
        glob_max = 0
        prev = -1
        prev_cnt = 0
        for f in fruits:
            if f in par:
                curr_max += 1
                if f == prev:
                    prev_cnt +=1 
                else:
                    prev = f
                    prev_cnt = 1
            else:
                par = {prev,f}
                curr_max = prev_cnt +1
                prev = f
                prev_cnt = 1
            glob_max = max(glob_max,curr_max)

        return glob_max


        