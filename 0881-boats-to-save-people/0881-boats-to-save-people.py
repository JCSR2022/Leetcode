class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Aproach: O[nLog(n)] because sorting
        # sort the array , greedy on hevy and lighters persons
        
        people.sort()
     
        l = 0 
        r = len(people)-1
        
        #print(people)
        
        count = 0
        while l <= r:
            #print(people[l],people[r],people[r]+people[l] <= limit )
            if people[r]+people[l] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
                
            count += 1
    
        return count