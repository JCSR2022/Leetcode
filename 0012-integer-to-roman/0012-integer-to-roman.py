class Solution:
    def intToRoman(self, num: int) -> str:
        unidades = ['','I', 'II', 'III', 'IV','V','VI','VII','VIII','IX']
        decenas = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        centenas = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        mil = ['','M','MM','MMM', 'I\u0056\u0305','\u0056\u0305','\u0056\u0305M',
               '\u0056\u0305MM','\u0056\u0305MMM', 'I\u0058\u0305']
        conv_4dig = [mil ,centenas,decenas,unidades]

        str_num = str(num)
        conv_dig = conv_4dig[-len(str_num):]

        ans = ""
        for i,digito in enumerate(str(num)):
            #print(i,digito, conv_dig[i][int(digito)-1])
            #if int(digito) != 0:
            ans = ans + conv_dig[i][int(digito)]

        return ans

        