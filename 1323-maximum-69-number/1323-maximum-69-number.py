class Solution:
    def maximum69Number (self, num: int) -> int:
        
        # str_num = [  digit  for digit in str(num)]
        # for i,digit in enumerate(str_num):
        #     if digit == "6":
        #         str_num[i] = "9"
        #         break

        # return int("".join(str_num))
        
        #----------------------------------------------------

        str_num = str(num)
        indx = str_num.find("6")
        if indx>=0:
            return  int(str_num[:indx]+'9'+str_num[indx+1:])
        else:
            return num
