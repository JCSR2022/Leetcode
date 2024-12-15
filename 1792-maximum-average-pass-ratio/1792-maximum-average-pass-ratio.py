class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # aproach:
        # 1. calculate actual %
        # 2 use a heap, add extra estudent always to min heap
        
        
        # heap order by pass_ratio first and later for total studendts
        # so have better impact adding a student
        
#         heap = [ (act_pass/total,act_pass,total) for act_pass, total in classes   ]
        
#         heapq.heapify(heap)
        
#         while extraStudents > 0:
#             print(heap)
#             _,act_pass,total =  heapq.heappop(heap)
            
#             heapq.heappush(heap,((act_pass+1)/(total+1), act_pass+1, total+1))
            
#             extraStudents -= 1
            
#         print(heap)
            
#         return sum( [pass_ratio for pass_ratio,_,_ in heap ]  )/len(heap)


#buena idea mal aplicada
#-----------------------------------------------------------------------------


#         def find_ratio_increment(index):
#             actual_ratio = classes[index][0]/classes[index][1]
#             new_ratio = (classes[index][0]+1)/(classes[index][1]+1)
#             #print(actual_ratio,new_ratio)
#             return new_ratio-actual_ratio
        
#         heap = [(-find_ratio_increment(i),i) for i in range(len(classes)) ]
#         heapq.heapify(heap)
    
#         while extraStudents > 0:
            
#             _,index =  heapq.heappop(heap)
            
#             classes[index][0] +=1
#             classes[index][1] +=1
            
#             heapq.heappush(heap,(-find_ratio_increment(index),index))
            
#             extraStudents -= 1
            
        
#         return sum([act_pass/total for act_pass,total in classes])/len(classes)
        

    #Faster version:

#         heap = [(passi/totali - (passi+1)/(totali+1),i) for i,(passi,totali) in enumerate(classes) ]
#         heapq.heapify(heap)
    
#         for i in range(extraStudents):
            
#             _,index =  heapq.heappop(heap)
            
#             classes[index][0] +=1
#             classes[index][1] +=1
            
#             heapq.heappush(heap,( classes[index][0]/classes[index][1]- (classes[index][0]+1)/(classes[index][1]+1),index))
            
        
#         return sum([act_pass/total for act_pass,total in classes])/len(classes)       
        

        n = len(classes)
        impacts = [(p/t - ((p+1)/(t+1)), p, t) for p,t in classes]
        heapq.heapify(impacts)

        for _ in range(extraStudents):
            impact, passes, total = heapq.heappop(impacts)
            passes +=1
            total +=1
            heapq.heappush(impacts, (passes/total - ((passes+1)/(total+1)), passes, total))

        percents = [p/t for _,p,t in impacts]
        return mean(percents)


