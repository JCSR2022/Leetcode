class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        #using fact are distinct
        hash_map = {h:n  for n,h in zip(names,heights) }
        
        heights.sort(reverse = True)
        
        return [ hash_map[h] for h in heights  ]
        
        
        
        # name_heig = [ [n,h]  for n,h in  zip(names,heights)]
        # sorted_name_heig = sorted(name_heig, key = lambda x:x[1], reverse= True)
        # return [ n[0] for n in sorted_name_heig  ]
        