class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
#     # brute, brute force
#         # base cases:
#         if len(trust) == 0:
#             if n == 1:
#                 return 1
#             else:
#                 return -1

#         if len(trust) == 1:
#             return trust[0][1]

#         # hash table
#         dicc_trust = {} #person,check_judge
#         for person,check_judge in trust:
#             if person not in dicc_trust:
#                 dicc_trust[person] = [check_judge]
#             else:
#                 dicc_trust[person].append(check_judge)

#         #cond_1 and cond_3:
#         if len(dicc_trust) == n-1:
#             posible_judge = int (n*(n+1)/2 - sum(dicc_trust.keys()))
#         else:
#             return -1

#         #Cond_2 and cond_3:
#         set_trusted = [set(sublista) for sublista in dicc_trust.values()]
#         interseccion = set.intersection(*set_trusted)
        
#         if  len(interseccion) == 1  and posible_judge in interseccion:
#             return posible_judge
#         else:
#             return -1


        # secund option
#         incoming = {i:0 for i in range(1,n+1)}
#         outgoing = {i:0 for i in range(1,n+1)}

#         for person,trusted in trust:
#             incoming[trusted] += 1
#             outgoing[person] += 1

#           # cond 1
#         trust_nobody = [key for key, value in outgoing.items() if value == 0]
        

#         #cond 2
#         trust_by_Everybody = [key for key, value in incoming.items() if value == n-1]
        
#         if trust_nobody == trust_by_Everybody:
#             return trust_nobody[0]
#         else:
#             return -1

        if len(trust) == 0:
            if n == 1:
                return 1
            else:
                return -1

        incoming = defaultdict(int)
        outgoing = defaultdict(int)
        
        for source,destination in trust:
            outgoing[source] += 1
            incoming[destination] += 1
            
        for i in range(1+n+1):
            if outgoing[i] == 0 and incoming[i] == n-1:
                return i
        return -1
            
        
        
        

        

        
                
                
                
                
            
            
            
            
            
            
            
        