class Fancy:
    #  y = m*x+c
    #  (y-c)/m = x
    

    def __init__(self):
        self.arr = []
        self.mult = 1
        self.const = 0
        self.mod = 10**9+7

    def append(self, val: int) -> None:
        #self.arr.append(  ((val-self.const)/self.mult)% self.mod )        
        corect_val =  ((val-self.const)*pow(self.mult,-1,self.mod))%self.mod
        self.arr.append(corect_val)
    def addAll(self, inc: int) -> None:
        self.const = (self.const+inc)%self.mod 
        

    def multAll(self, m: int) -> None:
        
        self.const = (self.const*m)%self.mod
        self.mult = (self.mult*m)%self.mod
        

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr): return -1
        return int(self.arr[idx]*self.mult+self.const)%self.mod


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)