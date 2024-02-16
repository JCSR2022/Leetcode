class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
#         numbers = []
#         frecuency = []
#         for elem in arr:
#             if elem in numbers:
#                 frecuency[numbers.index(elem)] += 1
#             else:
#                 numbers.append(elem)
#                 frecuency.append(1)
        

#         if k == 0:
#             return len(frecuency)
        
#         frecuency.sort()
#         i = 0
#         for f in frecuency:
#             if f > k and k <= 0:
#                 break
#             else:
#                 k -= f
#                 if k>=0:
#                     i +=1

#         return len(frecuency)-i


        dicc = {}
        for elem in arr:
            if elem in dicc:
                dicc[elem] +=1
            else:
                dicc[elem] = 1

        if k == 0:
            return len(dicc)

        # Sort the dictionary by values in descending order
        sorted_dicc = dict(sorted(dicc.items(), key=lambda x: x[1], reverse=False))


        suma = 0
        i = 0
        for frec in sorted_dicc.values():
            suma += frec
            if suma > k:
                break
            else:
                i +=1


        return len(list(sorted_dicc.values())[i:])

        
