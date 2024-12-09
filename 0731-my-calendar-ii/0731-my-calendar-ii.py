class MyCalendarTwo:

    def __init__(self):
        self.calendar_times = []
        self.calendar_books = []
    
    def book(self, startTime: int, endTime: int) -> bool:
        #line swep sol:
        
        #insert start
        if startTime not in self.calendar_times:
            pos_start = bisect.bisect_right(self.calendar_times, startTime)
            self.calendar_times.insert(pos_start,startTime)
            self.calendar_books.insert(pos_start,1)
        else:
            pos_start = self.calendar_times.index(startTime)
            self.calendar_books[pos_start] +=1
    
        #insert end
        if endTime not in self.calendar_times:
            pos_end = bisect.bisect_right(self.calendar_times, endTime)
            self.calendar_times.insert(pos_end,endTime)
            self.calendar_books.insert(pos_end,-1)
        else:
            pos_end = self.calendar_times.index(endTime)
            self.calendar_books[pos_end] -=1    
            
        max_booking = 0
        for book in self.calendar_books:
            max_booking += book
            if max_booking > 2:
                self.calendar_books[pos_start] -= 1
                self.calendar_books[pos_end] += 1
                return False
            
        return True

            


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)


#-------------------------------------------------------------
    # def __init__(self):
    #     self.calendar_books = defaultdict(int) 
    
#     def book(self, startTime: int, endTime: int) -> bool:
#         self.calendar_books[startTime] += 1
#         self.calendar_books[endTime] -= 1
#         max_booking = 0
#         for time in sorted(self.calendar_books.keys()):
#             max_booking += self.calendar_books[time]
            
#             if max_booking > 2:
#                 self.calendar_books[startTime] -= 1
#                 self.calendar_books[endTime] += 1
#                 return False
            
#         return True



#--------------------------------------------------------------

# def book(self, startTime: int, endTime: int) -> bool:
#         #print()
#         cont_start = 0
#         cont_end = 0
#         for sched_start,sched_end in self.calendar:
#             #print(self.calendar,(startTime, endTime),(sched_start,sched_end),sched_start <= startTime < sched_end,sched_start < endTime <= sched_end, sched_start <= startTime < sched_end  or sched_start < endTime <= sched_end,cont_start,cont_end )
#             if sched_start <= startTime < sched_end:
#                 cont_start += 1
                
#             if sched_start < endTime <= sched_end:
#                 cont_end += 1  
                
#             if sched_start < startTime and endTime > sched_end:
#                 cont_start += 1
#                 cont_end += 1    
                
#             if cont_start == 2 or cont_end ==2 :
#                 return False
            
            
        
#         self.calendar.add((startTime, endTime))
#         return True    

#--------------------------------------------------------


#         if not self.calendar:
#             self.calendar.append( (0,startTime,endTime) )
#             return True
    
#         #print(self.calendar)
        

#         for i,(count_overlaps,sched_start,sched_end) in enumerate(self.calendar):
#             if max(sched_start,startTime) < min(sched_end, endTime):
#                 if count_overlaps == 2:
#                     return False
#                 else:
#                     self.calendar[i] = (count_overlaps+1,sched_start,sched_end)
#                     return True
           
#         self.calendar.append( (0,startTime,endTime) )
#         return True    

