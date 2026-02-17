class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        # H = [8,4,2,1,0]
        # M = [32,16,8,4,2,1]

        # has_bits_min = {}
        # for i in range(60):
        #   print(i,bin(i),(bin(i)[2:]).count('1'))
        #   if (bin(i)[2:]).count('1') in has_bits_min :
        #     has_bits_min[(bin(i)[2:]).count('1')].append(str(i).zfill(2))
        #   else:
        #     has_bits_min[(bin(i)[2:]).count('1')] = [str(i).zfill(2)]
        # print(has_bits_min)
#------------------------------------------------------
#con este se representa hasta las 12
        # hash_bits_h = {0: ['0'], 1: ['1', '2', '4', '8'], 2: ['3', '5', '6', '9', '10', '12'], 3: ['7', '11']}
        # hash_bits_min =  {0: ['00'], 1: ['01', '02', '04', '08', '16', '32'], 2: ['03', '05', '06', '09', '10', '12', '17', '18', '20', '24', '33', '34', '36', '40', '48'], 3: ['07', '11', '13', '14', '19', '21', '22', '25', '26', '28', '35', '37', '38', '41', '42', '44', '49', '50', '52', '56'], 4: ['15', '23', '27', '29', '30', '39', '43', '45', '46', '51', '53', '54', '57', '58'], 5: ['31', '47', '55', '59']}
        
        # ans = []
        # for h in range(turnedOn+1):
        #     if h in hash_bits_h and turnedOn-h in hash_bits_min:
        #         for curr_h in hash_bits_h[h]:
        #             for curr_min in hash_bits_min[turnedOn-h]:
        #                 ans.append(curr_h+':'+curr_min )

        # return ans


#con este se representa hasta las 11
        hash_bits_h = {0: ['0'], 1: ['1', '2', '4', '8'], 2: ['3', '5', '6', '9', '10'], 3: ['7', '11']}
        hash_bits_min =  {0: ['00'], 1: ['01', '02', '04', '08', '16', '32'], 2: ['03', '05', '06', '09', '10', '12', '17', '18', '20', '24', '33', '34', '36', '40', '48'], 3: ['07', '11', '13', '14', '19', '21', '22', '25', '26', '28', '35', '37', '38', '41', '42', '44', '49', '50', '52', '56'], 4: ['15', '23', '27', '29', '30', '39', '43', '45', '46', '51', '53', '54', '57', '58'], 5: ['31', '47', '55', '59']}
        
        ans = []
        for h in range(turnedOn+1):
            if h in hash_bits_h and turnedOn-h in hash_bits_min:
                for curr_h in hash_bits_h[h]:
                    for curr_min in hash_bits_min[turnedOn-h]:
                        ans.append(curr_h+':'+curr_min )

        return ans



















#--------------------ajjajaja solo etaba buscando las posibles combinaciones
        #valid h with amount of bits
        # has_bits_h = {}
        # for i in range(13):
        #   print(i,bin(i),(bin(i)[2:]).count('1'))
        #   if (bin(i)[2:]).count('1') in has_bits_h:
        #     has_bits_h[(bin(i)[2:]).count('1')] +=1
        #   else:
        #     has_bits_h[(bin(i)[2:]).count('1')] = 1
        # print(has_bits_h)
            
        # has_bits_h = {0: 1, 1: 4, 2: 6, 3: 2}
        # has_bits_min = {0: 1, 1: 6, 2: 15, 3: 20, 4: 14, 5: 4}

        # ans = 0
        # for h in range(turnedOn+1):
        #     curr_h = 0
        #     curr_min = 0
        #     if h in has_bits_h:
        #         curr_h = has_bits_h[h]
        #     if turnedOn-h in has_bits_min:
        #         curr_min = has_bits_min[turnedOn-h]
        #     ans += curr_h*curr_min
    
        # return ans 
#---------------------------------------------