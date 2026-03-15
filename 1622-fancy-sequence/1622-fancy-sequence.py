class Fancy:

    def __init__(self):
        self.arr = []
        self.mod = 10**9+7 

    def append(self, val: int) -> None:
        self.arr.append(val)
        
    def addAll(self, inc: int) -> None:
        for i in range(len(self.arr)):
            self.arr[i] +=inc
            self.arr[i] %=self.mod

    def multAll(self, m: int) -> None:
        for i in range(len(self.arr)):
            self.arr[i] *=m
            self.arr[i] %=self.mod
        
    def getIndex(self, idx: int) -> int:
        
        return self.arr[idx] if len(self.arr)>idx else -1

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)