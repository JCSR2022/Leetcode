class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        #take 2 edegs, check repited val thats the center
        
        for ed in edges[0]:
            if ed in edges[1]:
                return ed
        