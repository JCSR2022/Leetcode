class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            
            # new interval is less than min in intervals
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                #print("finish breaking for cycle")
                return res + intervals[i:]
               
            # new interval begin after this interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # new interval is in this interval
            else: 
                #merge intervals
                left = min(newInterval[0],intervals[i][0])
                right = max(newInterval[1],intervals[i][1])
                newInterval = [left,right]
                
            #print(res,newInterval)
            
        res.append(newInterval)
        #print("finish after complete for cycle")
        return res