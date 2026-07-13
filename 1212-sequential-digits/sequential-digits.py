class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        #create all solutions:
        #342   78540
        #max size = 5
        #3 size 3   345 if > low and <high
        #4 size 3   456 if > low and <high
        #5 size 3   567
        #6          678
        #7          789
        #8 not valid  n+size >10
        #1 size 4   1234  
        #2......... 2345
        #...
        #6          6789
        #7 not valid 

        size = len(str(low))
        ans = []
        while True:
            inc_val = 1
            while inc_val + size <= 10:
                curr_ans =  sum([ (inc_val+i)*10**(size-i-1) for i in range(size) ])
                if curr_ans > high:  
                    return ans
                if curr_ans >= low:
                    ans.append(curr_ans)
                inc_val +=1

            if curr_ans == 123456789: 
                return ans
            size +=1


        


