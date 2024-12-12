class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []
        

    def addNum(self, num: int) -> None:
        
        if  not self.left_heap:
            heappush(self.left_heap,-num)
            return
        
        if num > -self.left_heap[0]:
            heappush(self.right_heap,num)
            if len(self.right_heap) > len(self.left_heap):
                mid = -heappop(self.right_heap)
                heappush(self.left_heap,mid)
        else:
            heappush(self.left_heap,-num)
            if len(self.left_heap) > len(self.right_heap):
                mid = -heappop(self.left_heap)
                heappush(self.right_heap,mid)

    def findMedian(self) -> float:
        if len(self.left_heap) > len(self.right_heap):
            return -self.left_heap[0]  
        
        elif len(self.left_heap) < len(self.right_heap):
            return self.right_heap[0]    
        
        else:
            return (self.right_heap[0]-self.left_heap[0])/2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()