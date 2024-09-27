class MyCalendarTwo:

    def __init__(self):
        self.time = [-1,float("inf")]
        self.count_act = [0,0]
        
    def book(self, start: int, end: int) -> bool:

        #insert new act:
        if start not in self.time:
            L = bisect_left(self.time,start)
            self.time.insert(L,start)
            self.count_act.insert(L,1)
        else:
            L = self.time.index(start)
            self.count_act[L] +=1

        if end not in self.time:
            R = bisect_left(self.time,end)
            self.time.insert(R,end)
            self.count_act.insert(R,-1)
        else:
            R = self.time.index(end)
            self.count_act[R] -=1
        
        
#         print(start,end)
#         print(self.time)
#         print(self.count_act)
#         print( [ self.time[i] for i in range(L,R+1)])
#         print( [ self.count_act[i] for i in range(L,R+1)])
        
        
        #check valid insertion, correct is not valid
        cont = 0
        for act in [self.count_act[i] for i in range(R+1)]:
            cont +=act
            if cont > 2:
                self.count_act[L] -=1
                self.count_act[R] +=1
                #print("not valid")
                return False
            
        #print()
        return True
        
            

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)