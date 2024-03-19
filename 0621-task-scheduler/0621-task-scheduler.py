from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Aproach: 
        # 1.create a hasmap of tasks
        # 1.1. sort hasmap
        # 2.create a list of size n to put the last n tasks
        # 2.2 create a cont of tasks or idle, contActivities
        # 3.go recursivly tru hasmap decresing the tasks until cero then delete
        # 4. finish when hashmap is empthy
        
        
#         HashTasks = Counter(tasks)
#         #HashTasks = dict(sorted(HashTasks.items(), key=lambda item: item[1],reverse = True))
        
#         lastTasks =[None]*n
#         contActivities = 0
        
        
#         while HashTasks:
#             print(HashTasks,lastTasks, contActivities)
            
#             isTaskdone = False
            
#             #try to do the most repited task on HashTasks if not , the subsecuent
            
# #             listOfTasks = list(HashTasks.keys()).copy()
            
# #             for task in listOfTasks:
        
# #                 if task not in lastTasks:
# #                     HashTasks[task] -= 1
# #                     if HashTasks[task] == 0:
# #                         del (HashTasks[task])
                    
# #                     lastTasks.append(task) 
# #                     lastTasks = lastTasks[1:]
                
# #                     isTaskdone = True
# #                     contActivities +=1
# #                     break
            
#             HashTasksCopy = HashTasks.copy()
#             while HashTasksCopy:
#                 task  = max(HashTasksCopy, key=HashTasksCopy.get)
                
#                 if task not in lastTasks:
#                     HashTasks[task] -= 1
#                     if HashTasks[task] == 0:
#                         del (HashTasks[task])  
                
#                     lastTasks.append(task) 
#                     lastTasks = lastTasks[1:]
                
#                     isTaskdone = True
#                     contActivities +=1
#                     break
#                 else:
#                     del (HashTasksCopy[task]) 

#             if not isTaskdone:
#                 lastTasks.append(None) 
#                 lastTasks = lastTasks[1:]
#                 contActivities +=1
                    
            
#         return contActivities

            #Secund aproach Maxheap and deque
    
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
#         print(count)
#         print(maxHeap)
        
        time = 0
        q = deque() # pairs of [-cnt,idleTime]
        
        while maxHeap or q:
            time  +=1
            
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
                
        return time    
            
                
                
        
        
        
        
        
        
        
        
        
        
        return 0
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        