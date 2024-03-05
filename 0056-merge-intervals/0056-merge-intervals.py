class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # 1 sort intervals 
        # 2 create a new array ans = []
        # 3 create inic =interval[0]
        # 4 check  if inic can merge whit interval[i]
        #     if can merge save merged as inic 
        #     repite step 4 with interva[i+1] untile i==len(intervals)-1
        
        
        # time O(nLog(n)) for sorting inntervals
        
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])

        i = 0
        temp = intervals[i]
        ans = []
        while i < len(intervals)-1:
            i +=1
            if temp[1] >= intervals[i][0]:
                temp = [temp[0],max(intervals[i][1],temp[1] )]
            else:
                ans.append(temp)
                temp = intervals[i]
        ans.append(temp)
        
        return ans

    
        
        