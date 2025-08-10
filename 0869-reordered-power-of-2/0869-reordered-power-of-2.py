class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        #aproach
        # find digits in all power of two until 10**9 digits, 
        # compare cont digits

        # i = 0
        # power2Num = 1
        # dig_count = set()
        # while power2Num < 10**9:
        #     curr_count = [0]*10
        #     for digit in str(power2Num):
        #         curr_count[int(digit)] +=1
        #     dig_count.add(tuple(curr_count))
        #     i +=1
        #     power2Num = 2**i

        # curr_count = [0]*10
        # for digit in str(n):
        #         curr_count[int(digit)] +=1
        

        # return tuple(curr_count) in dig_count

#-----------------------------------------------
        

        n_count = [0]*10
        for digit in str(n):
                n_count[int(digit)] +=1
        n_count = tuple(n_count)


        i = 0
        power2Num = 1
        dig_count = set()
        while power2Num < 10**9:
            curr_count = [0]*10
            for digit in str(power2Num):
                curr_count[int(digit)] +=1
            if tuple(curr_count) == n_count:
                return True
            i +=1
            power2Num = 2**i

        return False

        




        