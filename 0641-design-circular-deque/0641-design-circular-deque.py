class MyNode:
    def __init__(self,val: int):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.max_nodes = k
        self.num_nodes = 0
        self.head = MyNode(None)
        self.tail = MyNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.nodes = [ MyNode(None) for _ in range(k) ]
        
        
    def insertFront(self, value: int) -> bool:
        if self.num_nodes < self.max_nodes:
            self.num_nodes +=1
            node = self.nodes.pop()
            node.val = value
            node.prev = self.head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            return True
        return False
        
        
        
    def insertLast(self, value: int) -> bool:
        if self.num_nodes < self.max_nodes:
            self.num_nodes +=1
            node = self.nodes.pop()
            node.val = value
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node
            return True
        return False
        
        
        
    def deleteFront(self) -> bool:
         if self.num_nodes > 0:
            self.num_nodes -= 1
            self.nodes.append(self.head.next)
            self.head.next.next.prev = self.head
            self.head.next = self.head.next.next
            return True
         return False
            

        
    def deleteLast(self) -> bool:
        if self.num_nodes > 0:
            self.num_nodes -= 1
            self.nodes.append(self.tail.prev)
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
            return True
        return False
            
        

    def getFront(self) -> int:
        if self.num_nodes > 0:
            return self.head.next.val
        return -1
        

    def getRear(self) -> int:
        if self.num_nodes > 0:
            return self.tail.prev.val
        return -1
        

    def isEmpty(self) -> bool:
        if self.num_nodes == 0:
            return True
        return False
        
    def isFull(self) -> bool:
        if self.num_nodes == self.max_nodes:
            return True
        return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()