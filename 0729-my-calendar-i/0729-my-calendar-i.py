class MyCalendar:

    def __init__(self):
        self.events = []

    def start_bin_search(self, start):
        if start <= self.events[0][0]:
            return True, -1
        l = 0
        r = len(self.events)-1

        while l <= r:
            mid = (l+r)//2
            # print(l,r)

            if (mid+1 < len(self.events) and self.events[mid+1][0] == start):
                return False, -1
            if self.events[mid][1] <= start and (mid+1 >= len(self.events) or self.events[mid+1][0] > start):
                return True, mid
            elif self.events[mid][1] > start:
                r = mid-1
            else:
                l = mid+1
        
        return False, -1

    def book(self, start: int, end: int) -> bool:
        if not self.events:
            self.events.append([start, end])
            # print(self.events, True, start, end)
            return True
        start_possible, index = self.start_bin_search(start)

        if start_possible:
            if index+1 >= len(self.events) or self.events[index+1][0] >= end:
                self.events.insert(index+1, [start,end])
                # print(self.events, True, start, end)
                return True
        # print(self.events, False, start, end)
        return False

        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)