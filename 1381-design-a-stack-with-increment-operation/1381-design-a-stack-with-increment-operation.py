class CustomStack:
    def __init__(self, n: int):
        self.n, self.stack, self.inc = n, [], []

    def push(self, x: int) -> None:
        if len(self.stack) < self.n: self.stack.append(x), self.inc.append(0)

    def pop(self) -> int:
        if not self.stack: return -1
        if len(self.inc) > 1: self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        if self.inc: self.inc[min(k, len(self.inc)) - 1] += val








# class MyNode:
#     def __init__(self,val= None):
#         self.val = val
#         self.next = None

        
# class CustomStack:
#     def __init__(self, maxSize: int):
#         self.maxSize = maxSize
#         self.root = MyNode()
#         self.nod_cont = 0
        
#     def push(self, x: int) -> None:
#         if self.nod_cont == self.maxSize:
#             return None
#         self.nod_cont +=1
        
#         node = MyNode(x)
#         node.next = self.root.next
#         self.root.next = node
        

#     def pop(self) -> int:
#         if self.root.next == None:
#             return -1
#         self.nod_cont -= 1
        
#         val = self.root.next.val
#         self.root.next = self.root.next.next
#         return val
        
        

#     def increment(self, k: int, val: int) -> None:
#         node = self.root.next
#         skip_nodes = max(0,self.nod_cont-k)
#         while node :
#             if skip_nodes != 0:
#                 skip_nodes -= 1 
#             else:
#                 node.val += val
#             node = node.next
            
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)