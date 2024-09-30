
#brute force , not O(1):
from collections import Counter

class AllOne:

    def __init__(self):
        self.min_string = ""
        self.max_string = ""
        self.data = Counter()
        
        
    def inc(self, key: str) -> None:
    
        self.data[key] += 1
        
        # Obtener el key con mayor repetición
        self.max_string = max(self.data, key=self.data.get)

        # Obtener el key con menor repetición
        self.min_string = min(self.data, key=self.data.get)

        #print(self.data,self.max_string,self.min_string  )
        
        
        
    def dec(self, key: str) -> None:
        self.data[key] -= 1
        
        if self.data[key] == 0:
            del self.data[key] 
            
        if len(self.data) == 0:
            self.max_string = ""
            self.min_string = ""
        else:
            self.max_string = max(self.data, key=self.data.get)
            self.min_string = min(self.data, key=self.data.get)

        #print(self.data,self.max_string,self.min_string  )
        
        
        
    def getMaxKey(self) -> str:
        
        return self.max_string 
        

    def getMinKey(self) -> str:
        return self.min_string 
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()