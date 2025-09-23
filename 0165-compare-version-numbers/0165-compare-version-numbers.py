from itertools import zip_longest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

            ver1 = [ int(n) for n in version1.split(".")]
            ver2 = [ int(n) for n in version2.split(".")]

            #print(ver1)
            #print(ver2)

            for v1,v2 in zip_longest(ver1, ver2, fillvalue=0):
                #print(v1,v2)
                if v1 < v2:
                    return -1
                if v1 > v2:
                    return 1

            return 0




























        # ver1 = [int(i) for i in version1.split('.')]
        # ver2 = [int(i) for i in version2.split('.')]
        # #print(ver1)
        # #print(ver2)
        # #print(list(zip_longest(ver1,ver2, fillvalue=0)))
        
        
        # for v1, v2 in zip_longest(ver1,ver2,fillvalue=0):
        #     if v1 < v2:
        #         return -1
        #     elif v1 > v2:
        #         return 1
        
        # return 0
        