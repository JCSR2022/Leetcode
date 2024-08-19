from collections import deque

class Solution:
    def minSteps(self, n: int) -> int:
        
        #BFS!!!!
        # q values :
        # [num_elements_on_screen, num_elements_on_copy]
        
        q = deque()
        
        start = (1,0)
        q.append(start)
        
        operations = {}
        operations[start] = 0
        
        
        
        while True:
            on_screen, on_copy = q.popleft()
            ops = operations[(on_screen, on_copy)]
            
            if on_screen == n :
                return ops
 
            #process a copy operation
            if (on_screen,on_screen) not in operations:
                operations[(on_screen,on_screen)] = ops +1
                q.append((on_screen,on_screen))
                
            #process a paste operation
            if on_screen + on_copy <=n and  (on_screen + on_copy, on_copy) not in operations:
                operations[(on_screen + on_copy, on_copy)] = ops +1
                q.append((on_screen + on_copy, on_copy))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #try prime values ??? *n
        
        #1 .create a generator of prime values:
        #try n// prime untill == 1 , return i+ num trys
        
#         if n == 1:
#             return 0
        
#         def isprime(x):
#             if x <= 1:
#                 return False
#             if x <= 3:
#                 return True
#             if x % 2 == 0 or x % 3 == 0:
#                 return False
#             i = 5
#             while i * i <= x:
#                 if x % i == 0 or x % (i + 2) == 0:
#                     return False
#                 i += 6
#             return True
        
#         for i in range(2,n):
#             print("i:",i)
#             if isprime(i):
#                 for j in range(n//2):
#                     print("j",j)
#                     if j*i > n:
#                         break
#                     if j*i == n:
#                         return i+j
                    
                
            
        
        
        
        
        
        
        
        
#         def primeGenerator():
#             def isprime(n):
#                 if n <= 1:
#                     return False
#                 if n <= 3:
#                     return True
#                 if n % 2 == 0 or n % 3 == 0:
#                     return False
#                 i = 5
#                 while i * i <= n:
#                     if n % i == 0 or n % (i + 2) == 0:
#                         return False
#                     i += 6
#                 return True

#             n = 2
#             while True:
#                 if isprime(n):
#                     yield n
#                 n += 1

#         # Obtener los números primos del 1 al 1000
#         for primo in primeGenerator():
#             if primo > 1000:
#                 break




        
        
        
        
#         # binary tree??
#         #BRUTE , REALY BRUTE FORCE
        
#         if n == 1:
#             return 0
        
#         def find_copy_paste(i,x):
#             print("i,x,x == n:",i,x,x == n)
#             if x == n:
#                 return i+1
            
#             num = x
#             paste_op = 0
#             while num < n:
#                 num = num * 2
#                 paste_op += 2
#             print("num: ",num)
            
#             if num == n: 
#                 return i + paste_op
            
#             print("i+1,x+1",i+1,x+1)
#             return find_copy_paste(i+1,x+1)
                
                
#         return find_copy_paste(0,1)  