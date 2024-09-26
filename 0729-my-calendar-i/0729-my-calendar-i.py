class MyCalendar:

    def __init__(self):
        self.events = [(-2,-1),(float("inf"),float("inf"))]
        

    def book(self, start: int, end: int) -> bool:
        
        index = bisect.bisect_left(self.events , (start, end))
        
        
        if end <= self.events[index][0] and start >= self.events[index-1][1]:
            self.events.insert(index, (start, end))
            return True
        
        else:
            return False
    
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)