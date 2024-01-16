import random

class RandomizedSet:

    def __init__(self):
        self.set_input = set([])

    def insert(self, val: int) -> bool:
        if val in self.set_input:
            return False
        self.set_input.add(val)
        return True
            
    def remove(self, val: int) -> bool:
        if val not in self.set_input:
            return False
        self.set_input.remove(val)
        return True
        
            
    def getRandom(self) -> int:
        #if len(self.set_input)>0:
        return random.choice(list(self.set_input))



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()