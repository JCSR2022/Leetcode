class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        # aproach 1: make a hash map of all requisits of each course
        #    numCourses = 4, prerequisites = [[1,0],[2,1],[2,0],[3,1]]
        #       {3:[1], 2:[1,0] , 1:[0], 0:[]}
        #  for each elemt check: 
        #     1.if curse is not in the rest of curses_prerequisites of the hash table
        
#         hashCurses = {}
#         for course,prereq in prerequisites:
#             if course in hashCurses:
#                 hashCurses[course].append(prereq)
#             else:
#                 hashCurses[course] = [prereq]
        
#         print(hashCurses)
        
#         for course,prereq in hashCurses.items():
#             for pre in prereq:
#                 #print(course,pre)
#                 if pre in  hashCurses and course in hashCurses[pre]:
#                     return False
        
#         return True

# test case: 3   [[1,0],[0,2],[2,1]] 
# shows wrong aproach


# have to use graph aproach, DFS:
# [ [0,1],[0,2],[1,3],[1,4],[3,4]]
# 


        
        hashCurses = {i:[] for i in range(numCourses)}
        for course,prereq in prerequisites:
            hashCurses[course].append(prereq)

        print(hashCurses)
        
        visitSet = set()
        def dfs(current_course):
            if current_course in visitSet:
                return False
            
            if not hashCurses[current_course]:
                return True
            
            visitSet.add(current_course)
            for pre in hashCurses[current_course]:
                if not dfs(pre): return False 
            visitSet.remove(current_course)
            
            hashCurses[current_course] = []
            
            return True
            
            
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True



