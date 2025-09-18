# class TaskManager:

#     def __init__(self, tasks: List[List[int]]):

#         self.users_tasks = {}                    # userId: heap[(priority,taskId )]
#         self.task_users = defaultdict(list)      # taskId: [userId,priority]

#         for userId, taskId, priority in tasks: 
#             self.task_users[taskId] = [userId,priority]
#             if userId in self.users_tasks:
#                 heapq.heappush(self.users_tasks[userId],(-priority,-taskId))
#             else:
#                 self.users_tasks[userId] = [(-priority,-taskId)]


#     def add(self, userId: int, taskId: int, priority: int) -> None:
        
#         if userId in self.users_tasks:
#             heapq.heappush(self.users_tasks[userId],(-priority,-taskId))
#         else:
#             self.users_tasks[userId] = [(-priority,-taskId)]

#     def edit(self, taskId: int, newPriority: int) -> None:
#         userId = self.task_users[taskId][0]
#         priority = self.task_users[taskId][1]

#         temp = set()
#         while self.users_tasks[userId][0] != (-priority,-taskId):
#             temp.add( heapq.heappop(self.users_tasks[userId]) )

#         heapq.heappop(self.users_tasks[userId])
#         heapq.heappush(self.users_tasks[userId],(-newPriority,-taskId))

#         for task in temp:
#             heapq.heappush(self.users_tasks[userId],task)


#     def rmv(self, taskId: int) -> None:
#         userId = self.task_users[taskId][0]
#         priority = self.task_users[taskId][1]

#         temp = set()
#         while self.users_tasks[userId][0] != (-priority,-taskId):
#             temp.add( heapq.heappop(self.users_tasks[userId]) )

#         heapq.heappop(self.users_tasks[userId])

#         for task in temp:
#             heapq.heappush(self.users_tasks[userId],task)
        

#     def execTop(self) -> int:
#         notask = True
#         for user in self.users_tasks:
#             if self.users_tasks[user]:
#                 notask = False
#                 task = -self.users_tasks[user][0][1]
#                 del self.task_users[task]
#                 heapq.heappop(self.users_tasks[user]) 

#         if notask:
#             return -1


#imbecil!!!!!!
#------------------------------------------
from sortedcontainers import SortedSet
from sortedcontainers import SortedDict

class TaskManager:

    def __init__(self, tasks: List[List[int]]):

        self.task_users  =  defaultdict(tuple)          # {taskId: (userId,priority)}
        self.users_tasks = defaultdict(SortedSet)       # {userId:(-priority,-taskId)} 
        self.priority_tasks = SortedDict()              # {priority: (-taskId)} 

        for userId, taskId, priority in tasks: 
            self.task_users[taskId] =  (userId,priority)
            self.users_tasks[userId].add((-priority,-taskId) ) 
            if -priority in self.priority_tasks:
                self.priority_tasks[-priority].add(-taskId)
            else:
                self.priority_tasks[-priority] = SortedSet([-taskId])

        #self.printAll()

    def printAll(self):
        print("task:(userId,priority)",dict(self.task_users))
        print("userId:(-priority,-taskId)",dict(self.users_tasks))
        print("priority: (-taskId)",dict(self.priority_tasks))
        print()

    def add(self, userId: int, taskId: int, priority: int) -> None:

        self.task_users[taskId] =  (userId,priority)
        
        self.users_tasks[userId].add((-priority,-taskId) ) 
        
        if -priority in self.priority_tasks:
            self.priority_tasks[-priority].add(-taskId)
        else:
            self.priority_tasks[-priority] = SortedSet([-taskId])

        #self.printAll()

    def edit(self, taskId: int, newPriority: int) -> None:
        userId,priority = self.task_users[taskId]

        self.task_users[taskId] = (userId,newPriority)
        
        self.users_tasks[userId].discard( (-priority,-taskId)  )
        self.users_tasks[userId].add( (-newPriority,-taskId) ) 

        self.priority_tasks[-priority].discard(-taskId)
        if len(self.priority_tasks[-priority]) == 0:
            del self.priority_tasks[-priority]

        if -newPriority in self.priority_tasks:
            self.priority_tasks[-newPriority].add(-taskId)
        else:
            self.priority_tasks[-newPriority] = SortedSet([-taskId])

        #self.printAll()

    def rmv(self, taskId: int) -> None:
        userId,priority = self.task_users[taskId]

        del self.task_users[taskId]
        
        self.users_tasks[userId].discard( (-priority,-taskId)  )
        if len(self.users_tasks[userId]) == 0:
            del self.users_tasks[userId]

        self.priority_tasks[-priority].discard(-taskId)
        if len(self.priority_tasks[-priority]) == 0:
            del self.priority_tasks[-priority]

        #self.printAll()

    def execTop(self) -> int:
        if len(self.priority_tasks) == 0 :
            return -1

        tasks_highest_priority =  self.priority_tasks.peekitem(0)[1]
        taskId = -tasks_highest_priority[0]
        userId,priority = self.task_users[taskId]
        
        self.rmv(taskId)
        
        #self.printAll()

        return  userId




        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()