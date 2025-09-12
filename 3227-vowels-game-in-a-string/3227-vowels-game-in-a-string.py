class Solution:
    def doesAliceWin(self, s: str) -> bool:
        #aproach:

        # count vowels :
        # if count 0 return False
        # if count odd , retrurn True, Alice can take hole word//
        # if even check letters on last substring:
        #       no leeter before last vowel  axxxxx, return True, there is no way bob can take even vowels
        #       no leeter after  last vowel  xxxxa,return True,
        #       no leeters only vowel  a,return True,
        #       no leeters only vowel  xxxxaxxxx ("der" example 1),return True,

        count = sum( 1 for letter in s if letter in "aeiou" )
        
        return not count == 0 


