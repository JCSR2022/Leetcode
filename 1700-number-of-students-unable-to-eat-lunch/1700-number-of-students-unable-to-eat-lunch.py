class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """        
        students   = [1,1,1,0,0,1]
        sandwiches = [1,0,0,0,1,1]

        students   = [1,1,0,0,1]
        sandwiches = [0,0,0,1,1]

        students   = [1, 0, 0, 1, 1]
        sandwiches = [0, 0, 0, 1, 1]           
       
        students   = [0, 0, 1, 1, 1]
        sandwiches = [0, 0, 0, 1, 1]      
        
        
        students   = [0, 1, 1, 1]
        sandwiches = [0, 0, 1, 1]        
        
        students   = [1, 1, 1]
        sandwiches = [0, 1, 1]        
              
        """
            

        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                if sandwiches[0] in students:
                    students[:] = students[1:]+students[:1]
                else:
                    break
        return len(students)
            
            
            
            