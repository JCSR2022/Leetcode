class Solution:
    def maxDiff(self, num: int) -> int:
        
        #same as before, change the most significative digit

        N = len(str(num))

        
        #find min (need to change to 1, can not be cero)
        min_num = [ int(d) for d in str(num)]
        for i in range(N):
            if min_num[i] != 1 and min_num[i] != 0:
                dig_change = min_num[i]
                if i == 0:
                    val_change = 1
                else:
                    val_change = 0
                for j in range(i,N):
                      if min_num[j] == dig_change:
                        min_num[j] = val_change
                break
       
        min_num = int("".join([str(d) for d in min_num]))

 

        #find max
        max_num = [ int(d) for d in str(num)]
        for i in range(N):
            if max_num[i] != 9:
                dig_change = max_num[i]
                for j in range(i,N):
                    if max_num[j] == dig_change:
                        max_num[j] = 9
                break
        max_num = int("".join([str(d) for d in max_num ]))

        return max_num - min_num

        #print(max_num,min_num,max_num - min_num)

        
        




