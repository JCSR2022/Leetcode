class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        #https://www.youtube.com/watch?v=g2llEZ_JKt8
        
        workjob = namedtuple('WorkJob',['difficulty', 'profit'])
        
        worker.sort()
        
        
        
        work_queue = collections.deque(sorted(list(workjob(d,p) for d,p in zip(difficulty,profit)), key=lambda x:x[0]))
        
        current_profit = 0 
        best_job = 0
        
        for work in worker:
            while len(work_queue) > 0 and work_queue[0].difficulty <= work:
                wj = work_queue.popleft()
                best_job  = max(best_job ,wj.profit)
                                                         
            current_profit += best_job   
            
        return current_profit
        
        
        #greedy

#         diff_Prof = [ [d,p] for d,p in zip(difficulty,profit)]
#         diff_Prof.sort(key=lambda x: x[0])
        
#         maxProf = 0
#         for i,dp in enumerate(diff_Prof):
#             maxProf = max(maxProf,dp[1])
#             diff_Prof[i][1] = maxProf
        
#         print(diff_Prof)
        
#         diff = [d for d,p in diff_Prof]
#         print(diff)
        
        
#         def findMergeSort(n,diff):
#             l = diff[0]
#             r = diff[-1]
            
#             m = (l+r)//2
            
            
            
            
        
        
        
        
        return 0
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #brute force:
        # for each val in worker find max profits that correspond to difficulties less that val  
#         diff_Prof = [ (d,p) for d,p in zip(difficulty,profit)]
#         diff_Prof.sort(key=lambda x: x[0])
        
#         sum_profit = 0
        
#         for w in worker:
#             max_profit = 0
#             for d,p in diff_Prof:
#                 if d > w:
#                     break
#                 else:
#                     max_profit = max(max_profit,p)
#             sum_profit +=max_profit
        
#         return sum_profit
        
        
        
        
        
        #  minheap and maxheap 
        
        
        