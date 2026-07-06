class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        

        # flags = [0]*(10**5+1)

        # for l,r in intervals:
        #     flags[l] += 1
        #     flags[r] -= 1

        # flag = False
        # windows = 0
        # count = 0
        # for i in  flags:
        #     windows += i 
        #     if not flag and windows>0:
        #         flag = True
        #     if flag and windows == 0:
        #         flag = False
        #         count += 1

        # return count 
             

#---------------------------------------------
    
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        max_end = 0

        for start, end in intervals:
            if end > max_end:
                count += 1
                max_end = end

        return count