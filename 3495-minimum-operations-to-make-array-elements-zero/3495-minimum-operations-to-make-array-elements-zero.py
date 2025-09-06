class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        
        #first try brute force



        def find4Mult(num):
            cnt = 0
            while num != 0 :
                num = math.floor(num//4)
                cnt += 1
            return cnt


        def countOperations(l,r):
            #ans = []
            ans = 0
            i =  find4Mult(l)
            for num in range(l,r+1):
                if num >= 4**i:
                    i +=1
                #ans.append((num,i) )
                ans += i
            return math.ceil(ans/2)

        ans = 0
        for l,r in queries:
            ans += countOperations(l,r)

        return ans

            



        # print(  [ (i,math.floor(i//4),find4Mult(i) ) for i in range(1,4**3+1)])
        # print(  [ (i,math.floor(i//4),find4Mult(i) ) for i in range(4**4-1,4**4+2)])
        # print( countOperations(1,4**3+1) )
        # print( countOperations(4**4-1,4**4+2) )
      




