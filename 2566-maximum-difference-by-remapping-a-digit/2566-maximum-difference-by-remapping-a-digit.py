class Solution:
    def minMaxDifference(self, num: int) -> int:

        # to have max num need to change the mos signinficative digit to 9
        # and the other way arround for the opositive

        num_list = [ int(d) for d in str(num)]

        #find min:
        min_num = num_list.copy()
        digit_to_change = num_list[0]
        for i,n in enumerate(num_list):
                if n == digit_to_change:
                    min_num[i] = 0
        min_num = int( "".join([ str(d) for d in min_num ]))


        #find max
        digit_to_change = 9
        for n in num_list:
            if n !=9:
                digit_to_change = n
                break
        max_num = num_list.copy()
        if  digit_to_change != 9:
            for i,n in enumerate(num_list):
                if n == digit_to_change:
                    max_num[i] = 9
        max_num = int( "".join([ str(d) for d in max_num ]))
        

        return max_num-min_num



            

         
        
        