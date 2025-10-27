class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:


        prev_devices = 0
        total_connect = 0

        for row in bank:
            curr_devices = row.count("1")
            if curr_devices > 0 :
                total_connect += prev_devices * curr_devices
                prev_devices = curr_devices    

        return total_connect












































        # sum_lasers_beams =  0
        # sum_lasers = 0
        # for row in bank:
        #     cant_lasers = row.count('1')
        #     if cant_lasers != 0:
        #         if sum_lasers == 0:
        #             sum_lasers = cant_lasers
        #         else:
        #             sum_lasers_beams += sum_lasers*cant_lasers
        #             sum_lasers = cant_lasers
        # return sum_lasers_beams
            
        


        