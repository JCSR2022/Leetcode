#import queue
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
    
        # Brute force aproach 
        # move move through customers , add t+timestoservecx save time 
        # calculae mean
        # solve O(n)
        
        t = 0
        total = 0
       # times = []
        
        for arrival,order_time in customers:
            if t > arrival:
                total += t - arrival
            else:
                t = arrival
            
            total += order_time
            

            t += order_time
        
        return total / len(customers)

    

        
        
        
        
  ## @^$#Q^TW$%^$#^&^&^%#*UR&*R^(%^&(I*#$&#0))   
#         t = 1 
#         wating_time_per_cx = []
        
#         for cx_arr,cx_time in customers:
#             print(t, t - cx_arr,t - cx_arr+ cx_time )
            
#             t_before_prep = t - cx_arr
            
#             wating_time = t_before_prep + cx_time
            
#             wating_time_per_cx.append(wating_time)
            
#             t += wating_time
            
#         print(wating_time_per_cx)
        
#         return mean(wating_time_per_cx)
        
        
        
    
# #         t= 1
#         wating_time_cx = [0]
#         for cx_arr,cx_time in customers:
            
#             wating_time = t - cx_arr + cx_time 
            
#             print(t,wating_time)
#             t = wating_time + wating_time_cx[-1]
            
#             wating_time_cx.append(wating_time)
            
#         print(wating_time_cx)
        
#         return mean(wating_time_cx)
            
            
    
    #pq = queue.PriorityQueue()
    #pq.put((0,0))
    
    
    
    
    #         1 2 3 4 5 6 7 8 9 
    #         1 1 
    #           2 2 2 2 2 2  
    #               3 3 3 3 3 3 3
         
    
    
        