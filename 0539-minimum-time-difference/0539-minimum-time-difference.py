class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

#         int_timePoints = [ ]
#         for t in timePoints:
#             time = t.split(":")
#             int_timePoints.append(int(time[0])*60 +int(time[1]))
        
#         #print("##:",int_timePoints)
        
#         min_t = 1440
#         for i,time_i in enumerate(int_timePoints):
#             for j in range(i+1,len(int_timePoints)):

#                 if time_i == 0: time_i = 1440
#                 if  int_timePoints[j] == 0: int_timePoints[j] = 1440
                    
#                 #print(time_i,int_timePoints[j],(min_t,abs(time_i - int_timePoints[j])))
#                 min_t = min(min_t,abs(time_i - int_timePoints[j]) )
                
#         return min_t



    
        int_timePoints = [ ]
        for t in timePoints:
            time = t.split(":")
            int_timePoints.append(int(time[0])*60 +int(time[1]))
            
        int_timePoints.sort()
        #print(int_timePoints)

        min_t = min(int_timePoints[-1]-int_timePoints[0], abs(1440+int_timePoints[0]-int_timePoints[-1]))
        i = 0
        for j in range(1, len(int_timePoints)):
            min_t = min(min_t , int_timePoints[j]-int_timePoints[i])
            i = j
            
            
            
            
        return min_t 
            
        