class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        name_heig = [ [n,h]  for n,h in  zip(names,heights)]
        
        sorted_name_heig = sorted(name_heig, key = lambda x:x[1], reverse= True)
        
        return [ n[0] for n in sorted_name_heig  ]
        