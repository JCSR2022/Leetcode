class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:


        # base cases:
        if len(trust) == 0:
            if n == 1:
                return 1
            else:
                return -1
        
        
        
        if len(trust) == 1:
            return trust[0][1]


        # hash table
        dicc_trust = {} #person,check_judge
        for person,check_judge in trust:
            if person not in dicc_trust:
                dicc_trust[person] = [check_judge]
            else:
                dicc_trust[person].append(check_judge)

        #cond_1 and cond_3:
        if len(dicc_trust) == n-1:
            posible_judge = int (n*(n+1)/2 - sum(dicc_trust.keys()))
        else:
            return -1

        #Cond_2 and cond_3:
        set_trusted = [set(sublista) for sublista in dicc_trust.values()]
        interseccion = set.intersection(*set_trusted)
        
        if  len(interseccion) == 1  and posible_judge in interseccion:
            return posible_judge
        else:
            return -1

        
                
                
                
                
            
            
            
            
            
            
            
        